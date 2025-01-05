# 📝 Transcription App 🎙️
An advanced web application that converts audio to text and text to audio using **Azure Cognitive Services**. The app supports multiple languages, real-time transcription, voice synthesis, and provides an intuitive interface.

## 🔌 API Documentation

### Audio Transcription (Speech-to-Text)
```
POST /api/transcribe
```
**Request (multipart/form-data)**:
- `audio`: Audio file to transcribe
- `language`: Language code (e.g., "en-US", "it-IT")
- `output_format`: Output format (optional)
  - `verbatim`: Detailed transcription with timestamps [default]
  - `clean`: Clean text only
  - `subtitles`: Subtitles format (SRT)
  - `timestamps`: Text with start and end timestamps

**Response (JSON)**:
```json
{
    "transcription": "Transcribed text here",
    "file_path": "path/to/saved/file.txt"
}
```

### Voice Synthesis (Text-to-Speech)
```
POST /api/synthesize
```
**Request (JSON)**:
```json
{
    "text": "Text to convert to audio",
    "language": "en-US"
}
```
**Response**: 
- Audio file (WAV format)
- Content-Type: audio/wav

### Error Handling
All APIs return errors in this format:
```json
{
    "error": "Error description"
}
```

## ✨ Features

### 🎤 Audio to Text Transcription
* Support for uploaded audio files or microphone recordings
* Multiple languages (English, Italian, Spanish, etc.)
* Automatic speaker diarization
* Customizable output formats

### 🔊 Text to Audio Synthesis
* High-quality text-to-audio conversion
* WAV format downloads
* Multiple languages and voices available

### 📂 File Management
* Support for common audio formats (MP3, WAV)
* Direct browser recording

## 🛠️ Tech Stack

### Backend
* **Framework**: Flask
* **Main Libraries**:
  * `azure-cognitiveservices-speech`
  * `flask-cors`
  * `pydub`
  * `python-dotenv`

### Frontend
* **Framework**: Vue.js
* **Tools**:
  * `axios`
  * `tailwindcss`
  * `pinia`

## 🚀 Installation

### Prerequisites
* Python 3.8+
* Node.js 16+
* Azure Speech Service Account

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
# Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configuration:
* Copy `.env.example` to `.env`
* Add your Azure credentials:
```
AZURE_SPEECH_KEY=your_key
AZURE_SPEECH_REGION=your_region
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Access the app at `http://localhost:5173`

## 📜 License
MIT License

## 🤝 Contributing
Contributions are welcome! Fork the repository and submit a pull request.




# 📝 Transcription App 🎙️
Un'applicazione web avanzata che converte l'audio in testo e il testo in audio utilizzando **Azure Cognitive Services**. L'app supporta più lingue, trascrizione in tempo reale, sintesi vocale e offre un'interfaccia intuitiva.

## 🔌 Documentazione API

### Trascrizione Audio (Speech-to-Text)
```
POST /api/transcribe
```
**Richiesta (multipart/form-data)**:
- `audio`: File audio da trascrivere
- `language`: Codice lingua (es. "it-IT", "en-US")
- `output_format`: Formato output (opzionale) 
  - `verbatim`: Trascrizione dettagliata con timestamp [default]
  - `clean`: Solo testo pulito
  - `subtitles`: Formato sottotitoli (SRT)
  - `timestamps`: Testo con timestamp di inizio e fine

**Risposta (JSON)**:
```json
{
    "transcription": "Testo trascritto qui",
    "file_path": "percorso/al/file/salvato.txt"
}
```

### Sintesi Vocale (Text-to-Speech)
```
POST /api/synthesize
```
**Richiesta (JSON)**:
```json
{
    "text": "Testo da convertire in audio",
    "language": "it-IT"
}
```
**Risposta**: 
- File audio (formato WAV)
- Content-Type: audio/wav

### Gestione Errori
Tutte le API restituiscono gli errori in questo formato:
```json
{
    "error": "Descrizione dell'errore"
}
```

## ✨ Funzionalità

### 🎤 Trascrizione da Audio a Testo
* Supporto per file audio caricati o registrazioni dal microfono
* Multiple lingue (Italiano, Inglese, Spagnolo, etc.)
* Diarizzazione automatica dei parlanti
* Formati di output personalizzabili

### 🔊 Sintesi da Testo a Audio
* Conversione testo in audio di alta qualità
* Download in formato WAV
* Multiple lingue e voci disponibili

### 📂 Gestione File
* Supporto formati audio comuni (MP3, WAV)
* Registrazione diretta dal browser

## 🛠️ Stack Tecnologico

### Backend
* **Framework**: Flask
* **Librerie principali**:
  * `azure-cognitiveservices-speech`
  * `flask-cors`
  * `pydub`
  * `python-dotenv`

### Frontend
* **Framework**: Vue.js
* **Strumenti**:
  * `axios`
  * `tailwindcss`
  * `pinia`

## 🚀 Installazione

### Prerequisiti
* Python 3.8+
* Node.js 16+
* Account Azure Speech Service

### Setup Backend
1. Clona il repository:
```bash
git clone https://github.com/your-username/transcription-app.git
cd transcription-app/backend
```

2. Crea e attiva l'ambiente virtuale:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

3. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

4. Configurazione:
* Copia `.env.example` in `.env`
* Aggiungi le tue credenziali Azure:
```
AZURE_SPEECH_KEY=la_tua_chiave
AZURE_SPEECH_REGION=la_tua_regione
```

### Setup Frontend
```bash
cd frontend
npm install
npm run dev
```

Accedi all'app su `http://localhost:5173`

## Avvio in locale una volta installata sul proprio pc
Sì, esattamente! Seguendo questi passaggi, avvierai sia il frontend che il backend della tua applicazione devi utilizzare due prompt separati uno per fe e uno per be

---

### **Avvio del Frontend**
1. Spostati nella directory del frontend:
   ```bash
   cd transcription-app
   cd frontend
   ```

2. Avvia il server di sviluppo:
   ```bash
   npm run dev
   ```

   Il frontend sarà accessibile, di solito, su `http://localhost:5173`.

---

### **Avvio del Backend**
1. Spostati nella directory del backend:
   ```bash
   cd transcription-app
   cd backend
   ```

2. Crea l'ambiente virtuale (solo se non esiste già):
   ```bash
   python -m venv venv
   ```

3. Attiva l'ambiente virtuale:
   ```bash
   venv\Scripts\activate
   ```

4. Installa le dipendenze dal file `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. Avvia il backend:
   ```bash
   python app.py
   ```

---

### **Controllo**
1. Dopo aver avviato il frontend e il backend:
   - **Frontend**: Assicurati che sia accessibile su `http://localhost:5173`.
   - **Backend**: Di solito sarà accessibile su `http://127.0.0.1:5000` (o un'altra porta configurata nel tuo script `app.py`).

2. Testa la comunicazione tra il frontend e il backend (ad esempio, tramite una funzione di login o una chiamata API).

---

Se incontri problemi, condividi i messaggi di errore e ti aiuterò a risolverli! 😊

## 📜 Licenza
MIT License

## 🤝 Contributi
I contributi sono benvenuti! Fai una fork del repository e invia una pull request.

