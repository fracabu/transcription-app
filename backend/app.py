from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from azure.cognitiveservices.speech import (
    SpeechConfig, 
    SpeechSynthesizer, 
    AudioConfig, 
    SpeechRecognizer,
    ResultReason
)
from azure.cognitiveservices.speech.transcription import (
    ConversationTranscriber,
    ConversationTranscriptionEventArgs
)
from werkzeug.utils import secure_filename
from pydub import AudioSegment
import os
from dotenv import load_dotenv
import tempfile
import logging
import time
import gc
import io

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Directory per i file caricati e le trascrizioni
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'synthesized_audio')
TRANSCRIPTION_FOLDER = os.path.join(os.getcwd(), 'transcriptions')

# Crea le directory se non esistono
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TRANSCRIPTION_FOLDER, exist_ok=True)

# Configura Flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configurazioni Azure
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

def continuous_recognize_with_diarization(speech_config, audio_config):
    """Perform continuous speech recognition with diarization using numbered speakers."""
    transcriber = ConversationTranscriber(speech_config=speech_config, audio_config=audio_config)
    done = False
    all_results = []
    
    # Dizionario per mappare gli ID degli speaker ai numeri
    speaker_mapping = {}
    current_speaker_number = 1

    def handle_transcribed(evt: ConversationTranscriptionEventArgs):
        nonlocal current_speaker_number
        
        if evt.result.reason == ResultReason.RecognizedSpeech and evt.result.text:
            speaker_id = evt.result.speaker_id if evt.result.speaker_id else "Unknown"
            
            # Assegna un numero progressivo a ogni nuovo speaker
            if speaker_id not in speaker_mapping:
                speaker_mapping[speaker_id] = f"Speaker {current_speaker_number}"
                current_speaker_number += 1
            
            # Usa il numero assegnato allo speaker
            numbered_speaker = speaker_mapping[speaker_id]
            all_results.append(f"{numbered_speaker}: {evt.result.text}")
            logger.debug(f"Recognized chunk from {numbered_speaker}: {evt.result.text}")

    def stop_cb(evt):
        nonlocal done
        logger.debug("Recognition stopped.")
        done = True

    # Connect callbacks
    transcriber.transcribed.connect(handle_transcribed)
    transcriber.session_stopped.connect(stop_cb)
    transcriber.canceled.connect(stop_cb)

    # Start continuous recognition
    logger.debug("Starting continuous recognition with diarization...")
    transcriber.start_transcribing_async().get()
    
    # Wait for recognition to complete
    while not done:
        time.sleep(.5)
    
    # Stop recognition
    transcriber.stop_transcribing_async().get()
    
    # Clean up
    transcriber.dispose()
    gc.collect()
    
    return '\n'.join(all_results)

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    try:
        # Ottieni il file audio o video e la lingua dalla richiesta
        audio_file = request.files.get('audio')
        language = request.form.get('language', 'en-US')

        if not audio_file:
            return jsonify({'error': 'No audio file provided'}), 400

        logger.debug(f"Processing audio file: {audio_file.filename}")
        logger.debug(f"Selected language: {language}")

        # Salva il file audio nella cartella "synthesized_audio"
        input_path = os.path.join(UPLOAD_FOLDER, secure_filename(audio_file.filename))
        audio_file.save(input_path)
        logger.debug(f"File saved to: {input_path}")

        # Percorso del file WAV convertito
        wav_path = os.path.join(UPLOAD_FOLDER, f"{os.path.splitext(audio_file.filename)[0]}.wav")

        # Converti il file audio in formato WAV
        if not convert_to_wav(input_path, wav_path):
            raise Exception("Failed to convert audio file to WAV format")

        logger.debug(f"File converted to WAV: {wav_path}")

        # Crea la configurazione per Azure Speech Service
        speech_config = create_speech_config(language)
        audio_config = AudioConfig(filename=wav_path)

        # Esegui la trascrizione continua con diarizzazione
        logger.debug("Starting continuous transcription with diarization...")
        transcribed_text = continuous_recognize_with_diarization(speech_config, audio_config)
        logger.debug("Transcription completed")

        # Salva la trascrizione nella cartella "transcriptions"
        if transcribed_text:
            transcription_filename = f"{os.path.splitext(audio_file.filename)[0]}.txt"
            transcription_file = os.path.join(TRANSCRIPTION_FOLDER, transcription_filename)
            with open(transcription_file, 'w', encoding='utf-8') as f:
                f.write(transcribed_text)

            logger.debug(f"Transcription saved to: {transcription_file}")

            return jsonify({
                'transcription': transcribed_text,
                'file_path': transcription_file
            })
        else:
            return jsonify({'error': 'No speech could be recognized'}), 400

    except Exception as e:
        logger.error(f"Error in transcribe: {str(e)}")
        return jsonify({'error': str(e)}), 500

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
            safe_delete_file(temp_file_path)

if __name__ == '__main__':
    app.run(debug=True)
