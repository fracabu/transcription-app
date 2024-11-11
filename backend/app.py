from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from azure.cognitiveservices.speech import (
    SpeechConfig, 
    SpeechSynthesizer, 
    AudioConfig, 
    SpeechRecognizer,
    ResultReason
)
from pydub import AudioSegment
import os
from dotenv import load_dotenv
import tempfile
import logging
import wave
import io
import time
import gc

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Get Azure credentials from environment variables
speech_key = os.getenv('AZURE_SPEECH_KEY')
speech_region = os.getenv('AZURE_SPEECH_REGION')

logger.debug(f"Speech Key: {speech_key[:4]}...")
logger.debug(f"Speech Region: {speech_region}")

def create_speech_config(language):
    """Create speech configuration with the specified language."""
    speech_config = SpeechConfig(subscription=speech_key, region=speech_region)
    speech_config.speech_synthesis_language = language
    speech_config.speech_recognition_language = language
    return speech_config

def safe_delete_file(file_path, max_retries=5, delay=1):
    """Safely delete a file with retries."""
    if not file_path or not os.path.exists(file_path):
        return True

    for i in range(max_retries):
        try:
            gc.collect()
            os.close(os.open(file_path, os.O_RDONLY))
            os.unlink(file_path)
            logger.debug(f"Successfully deleted file: {file_path}")
            return True
        except Exception as e:
            if i == max_retries - 1:
                logger.error(f"Failed to delete file after {max_retries} attempts: {str(e)}")
                return False
            time.sleep(delay)
    return False

def convert_to_wav(input_path, output_path):
    """Convert audio file to WAV format with correct parameters."""
    try:
        audio = AudioSegment.from_file(input_path)
        if audio.channels > 1:
            audio = audio.set_channels(1)
        audio = audio.set_frame_rate(16000)
        audio.export(output_path, format='wav', parameters=[
            '-acodec', 'pcm_s16le',
            '-ar', '16000',
            '-ac', '1'
        ])
        logger.debug(f"Successfully converted audio to WAV: {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error converting audio: {str(e)}")
        return False

def continuous_recognize(speech_config, audio_config):
    """Perform continuous speech recognition for long audio files."""
    recognizer = SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    done = False
    all_results = []

    def handle_result(evt):
        if evt.result.reason == ResultReason.RecognizedSpeech and evt.result.text:
            all_results.append(evt.result.text)
            logger.debug(f"Recognized chunk: {evt.result.text}")

    def stop_cb(evt):
        nonlocal done
        logger.debug("Recognition stopped.")
        done = True

    # Connect callbacks
    recognizer.recognized.connect(handle_result)
    recognizer.session_stopped.connect(stop_cb)
    recognizer.canceled.connect(stop_cb)

    # Start continuous recognition
    logger.debug("Starting continuous recognition...")
    recognizer.start_continuous_recognition()
    
    # Wait for recognition to complete
    while not done:
        time.sleep(.5)
    
    # Stop recognition
    recognizer.stop_continuous_recognition()
    
    # Clean up
    recognizer.disposed = True
    del recognizer
    gc.collect()
    
    return ' '.join(all_results)

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    temp_files = []
    try:
        # Get the audio file and language from the request
        audio_file = request.files.get('audio')
        language = request.form.get('language', 'en-US')
        
        if not audio_file:
            return jsonify({'error': 'No audio file provided'}), 400
            
        logger.debug(f"Processing audio file: {audio_file.filename}")
        logger.debug(f"Selected language: {language}")
        
        # Create temporary files with explicit cleanup
        with tempfile.NamedTemporaryFile(delete=False) as input_file, \
             tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as wav_file:
            
            input_path = input_file.name
            wav_path = wav_file.name
            temp_files.extend([input_path, wav_path])
            
            # Save the uploaded file
            audio_file.save(input_path)
            
            # Convert to WAV with correct parameters
            if not convert_to_wav(input_path, wav_path):
                raise Exception("Failed to convert audio file to WAV format")
            
            # Create speech configuration
            speech_config = create_speech_config(language)
            
            # Create audio configuration
            audio_config = AudioConfig(filename=wav_path)
            
            # Perform continuous transcription
            logger.debug("Starting continuous transcription...")
            transcribed_text = continuous_recognize(speech_config, audio_config)
            logger.debug("Transcription completed")
            
            if transcribed_text:
                return jsonify({'transcription': transcribed_text})
            else:
                return jsonify({'error': 'No speech could be recognized'}), 400
            
    except Exception as e:
        logger.error(f"Error in transcribe: {str(e)}")
        return jsonify({'error': str(e)}), 500
    finally:
        # Clean up temporary files
        time.sleep(0.5)
        for file_path in temp_files:
            safe_delete_file(file_path)

@app.route('/api/synthesize', methods=['POST'])
def synthesize():
    temp_file_path = None
    synthesizer = None
    
    try:
        data = request.get_json()
        text = data.get('text', '')
        language = data.get('language', 'en-US')
        
        logger.debug(f"Synthesizing text in language: {language}")
        
        # Create speech configuration
        speech_config = create_speech_config(language)
        
        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
            temp_file_path = temp_file.name
            audio_config = AudioConfig(filename=temp_file_path)
            synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
            
            # Synthesize text
            logger.debug("Starting synthesis...")
            result = synthesizer.speak_text_async(text).get()
            logger.debug(f"Synthesis result reason: {result.reason}")
            
            if result.reason == ResultReason.SynthesizingAudioCompleted:
                # Read the generated audio file
                with open(temp_file_path, 'rb') as audio_file:
                    audio_data = audio_file.read()
                
                return send_file(
                    io.BytesIO(audio_data),
                    mimetype='audio/wav',
                    as_attachment=True,
                    download_name='synthesized_speech.wav'
                )
            else:
                raise Exception(f"Speech synthesis failed: {result.reason}")
            
    except Exception as e:
        logger.error(f"Error in synthesize: {str(e)}")
        return jsonify({'error': str(e)}), 500
    finally:
        if synthesizer:
            try:
                synthesizer.disposed = True
                del synthesizer
            except:
                pass
        
        gc.collect()
        
        if temp_file_path:
            time.sleep(0.5)
            safe_delete_file(temp_file_path)

if __name__ == '__main__':
    app.run(debug=True)