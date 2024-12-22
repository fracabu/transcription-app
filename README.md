# 📝 **Transcription App** 🎙️

Un'applicazione web avanzata che converte l'audio in testo e il testo in audio utilizzando **Azure Cognitive Services**. L'app supporta più lingue, trascrizione in tempo reale, sintesi vocale e offre un'interfaccia intuitiva per caricare file o registrare audio.

---

## ✨ **Funzionalità**

- **🎤 Trascrizione da Audio a Testo**:
  - Trascrivi file audio caricati o registrazioni dal microfono.
  - Supporta diverse lingue, tra cui Italiano, Inglese, Spagnolo e altre.
  - Genera trascrizioni in vari formati (verbatim, clean, sottotitoli, ecc.).
  - Diarizzazione per identificare i diversi speaker in una conversazione.

- **🔊 Sintesi da Testo a Audio**:
  - Converte il testo in audio sintetizzato di alta qualità.
  - Scarica i file audio generati in formato WAV.
  - Supporto per più lingue e voci.

- **📂 Caricamento File e Registrazione**:
  - Carica file audio in vari formati (MP3, WAV, ecc.).
  - Registra audio direttamente dal browser.

- **🌐 Interfaccia Utente**:
  - Design moderno e responsivo, sviluppato con Vue.js e TailwindCSS.
  - Messaggi di stato per le azioni dell'utente.
  - Dropdown per la selezione della lingua supportata.

---

## 🛠️ **Stack Tecnologico**

### Backend
- **Framework**: Flask
- **Librerie principali**:
  - `flask-cors`: Condivisione delle risorse tra domini diversi.
  - `azure-cognitiveservices-speech`: Integrazione con Azure Cognitive Services.
  - `pydub`: Elaborazione audio.
  - `dotenv`: Gestione delle variabili d'ambiente.
- **Endpoint API**:
  - `/api/transcribe`: Gestisce il caricamento dei file audio e restituisce la trascrizione.
  - `/api/synthesize`: Converte testo in audio e restituisce il file audio.

### Frontend
- **Framework**: Vue.js
- **Strumenti principali**:
  - `axios`: Comunicazione con le API.
  - `tailwindcss`: Styling.
  - `pinia`: Gestione dello stato.

---

## 🚀 **Installazione e Configurazione**

### Prerequisiti
- Python 3.8 o superiore
- Node.js 16 o superiore
- Account Azure Speech Service (con chiave API e regione)

### Configurazione del Backend
1. Clona il repository:
   ```bash
   git clone https://github.com/tuo-repo/transcription-app.git
   cd transcription-app/backend
   ```

2. Crea un ambiente virtuale e attivalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```

3. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura le variabili d'ambiente:
   - Crea un file `.env` nella directory `backend`:
     ```env
     AZURE_SPEECH_KEY=la_tua_chiave_azure_speech
     AZURE_SPEECH_REGION=la_tua_regione_azure_speech
     ```
   - Sostituisci `la_tua_chiave_azure_speech` e `la_tua_regione_azure_speech` con le tue credenziali Azure.

5. Avvia il server backend:
   ```bash
   python app.py
   ```

### Configurazione del Frontend
1. Vai nella directory `frontend`:
   ```bash
   cd ../frontend
   ```

2. Installa le dipendenze:
   ```bash
   npm install
   ```

3. Avvia il server di sviluppo:
   ```bash
   npm run dev
   ```

4. Apri l'app nel browser all'indirizzo `http://localhost:5173`.

---

## 🎯 **Utilizzo**

### Trascrizione da Audio a Testo
1. Seleziona una lingua dal menu a tendina.
2. Registra audio o carica un file audio.
3. Clicca sul pulsante **Trascrivi** per elaborare l'audio.
4. Visualizza e salva la trascrizione.

### Sintesi da Testo a Audio
1. Inserisci il testo nel campo di input.
2. Seleziona una lingua per la sintesi vocale.
3. Clicca su **Genera Audio** per scaricare l'audio sintetizzato.

---

## 🌍 **Lingue Supportate**
- Italiano - `it-IT`
- Inglese (USA) - `en-US`
- Spagnolo - `es-ES`
- Francese - `fr-FR`
- Tedesco - `de-DE`
- ...e molte altre (vedi l'elenco completo nell'app).

---

## 📜 **Licenza**
Questo progetto è distribuito sotto licenza MIT. Consulta il file LICENSE per maggiori dettagli.

---

## 🤝 **Contributi**
I contributi sono benvenuti! Fai un fork del repository e invia una pull request con i tuoi miglioramenti.

---

## ❤️ **Ringraziamenti**
- [Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/) per le funzionalità di trascrizione e sintesi vocale.
- [Pydub](https://pydub.com/) per l'elaborazione audio.

---

### ✨ **Divertiti a esplorare la potenza della trascrizione e sintesi vocale con Transcription App!**

