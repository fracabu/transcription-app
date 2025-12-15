<h1 align="center">Transcription App</h1>
<h3 align="center">Speech-to-Text & Text-to-Speech with Azure AI</h3>

<p align="center">
  <em>Multi-language audio transcription and voice synthesis</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white" alt="Vue.js" />
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/Azure_Cognitive-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white" alt="Azure" />
  <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind" />
</p>

<p align="center">
  :gb: <a href="#english">English</a> | :it: <a href="#italiano">Italiano</a>
</p>

---

<a name="english"></a>
## :gb: English

### Overview

An advanced web application that converts audio to text and text to audio using **Azure Cognitive Services**. Supports multiple languages, real-time transcription, voice synthesis, and provides an intuitive interface.

### Features

- **Speech-to-Text** - Upload audio files or record from microphone
- **Text-to-Speech** - High-quality voice synthesis with WAV download
- **Multi-Language** - English, Italian, Spanish, and more
- **Output Formats** - Verbatim, clean text, subtitles (SRT), timestamps
- **Speaker Diarization** - Automatic speaker identification

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/transcribe` | POST | Audio to text transcription |
| `/api/synthesize` | POST | Text to audio synthesis |

### Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Vue.js, Tailwind CSS, Pinia |
| Backend | Flask, Python 3.8+ |
| AI | Azure Cognitive Services |
| Audio | pydub |

### Quick Start

```bash
# Clone
git clone https://github.com/fracabu/transcription-app.git
cd transcription-app

# Backend
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Create .env
AZURE_SPEECH_KEY=your_key
AZURE_SPEECH_REGION=your_region

python app.py

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

Access at `http://localhost:5173`

---

<a name="italiano"></a>
## :it: Italiano

### Panoramica

Un'applicazione web avanzata che converte audio in testo e testo in audio usando **Azure Cognitive Services**. Supporta piu lingue, trascrizione real-time, sintesi vocale e offre un'interfaccia intuitiva.

### Funzionalita

- **Speech-to-Text** - Carica file audio o registra dal microfono
- **Text-to-Speech** - Sintesi vocale alta qualita con download WAV
- **Multi-Lingua** - Italiano, Inglese, Spagnolo e altre
- **Formati Output** - Verbatim, testo pulito, sottotitoli (SRT), timestamp
- **Diarizzazione** - Identificazione automatica parlanti

### Endpoint API

| Endpoint | Metodo | Descrizione |
|----------|--------|-------------|
| `/api/transcribe` | POST | Trascrizione audio in testo |
| `/api/synthesize` | POST | Sintesi testo in audio |

### Stack Tecnologico

| Layer | Tecnologia |
|-------|------------|
| Frontend | Vue.js, Tailwind CSS, Pinia |
| Backend | Flask, Python 3.8+ |
| AI | Azure Cognitive Services |
| Audio | pydub |

### Avvio Rapido

```bash
# Clone
git clone https://github.com/fracabu/transcription-app.git
cd transcription-app

# Backend
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Crea .env
AZURE_SPEECH_KEY=tua_chiave
AZURE_SPEECH_REGION=tua_regione

python app.py

# Frontend (nuovo terminale)
cd frontend
npm install
npm run dev
```

Accedi su `http://localhost:5173`

---

## Requirements

- Python 3.8+
- Node.js 16+
- Azure Speech Service account

## License

MIT

---

<p align="center">
  <a href="https://github.com/fracabu">
    <img src="https://img.shields.io/badge/Made_by-fracabu-8B5CF6?style=flat-square" alt="Made by fracabu" />
  </a>
</p>
