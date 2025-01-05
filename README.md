# 📝 Transcription App 🎙️

A powerful web application that converts audio to text and text to audio using **Azure Cognitive Services**. The app supports multiple languages, real-time transcription, voice synthesis, and provides an intuitive interface for file uploads or audio recording.

## ✨ Features

### 🎤 Audio to Text Transcription
* Transcribe uploaded audio files or microphone recordings
* Support for multiple languages including English, Italian, Spanish, and more
* Generate transcriptions in various formats (verbatim, clean, subtitles)
* Speaker diarization for multi-speaker conversations

### 🔊 Text to Speech Synthesis
* Convert text to high-quality synthesized audio
* Download generated audio files in WAV format
* Support for multiple languages and voices

### 📂 File Handling and Recording
* Support for various audio formats (MP3, WAV)
* Direct browser recording capabilities

### 🌐 User Interface
* Modern, responsive design built with Vue.js and TailwindCSS
* Real-time status updates
* Intuitive language selection

## 🛠️ Tech Stack

### Backend
* **Framework**: Flask
* **Key Libraries**:
  * `flask-cors`: Cross-domain resource sharing
  * `azure-cognitiveservices-speech`: Azure Cognitive Services integration
  * `pydub`: Audio processing
  * `python-dotenv`: Environment variables management

### Frontend
* **Framework**: Vue.js
* **Core Tools**:
  * `axios`: API communication
  * `tailwindcss`: Styling
  * `pinia`: State management

## 🚀 Getting Started

### Prerequisites
* Python 3.8+
* Node.js 16+
* Azure Speech Service account (API key and region)

### Backend Setup
1. Clone the repository:
```bash
git clone https://github.com/your-username/transcription-app.git
cd transcription-app/backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
   * Copy `.env.example` to `.env`
   * Add your Azure credentials in `.env`:
```
AZURE_SPEECH_KEY=your_azure_speech_key
AZURE_SPEECH_REGION=your_azure_region
```

5. Start the backend server:
```bash
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Access the app at `http://localhost:5173`

## 🌍 Supported Languages
* English (US) - `en-US`
* Italian - `it-IT`
* Spanish - `es-ES`
* French - `fr-FR`
* German - `de-DE`
* And many more (see complete list in app)

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ❤️ Acknowledgments
* Azure Cognitive Services for transcription and synthesis capabilities
* Open source community for amazing tools and libraries

---
Made with ❤️ by [fracabu]

#Azure #Accessibility #OpenSource #WebDevelopment

