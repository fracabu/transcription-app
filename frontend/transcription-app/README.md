
# 🎙️ Transcription App

![image](https://github.com/user-attachments/assets/92112801-2b04-429a-b43c-2a2a4d0f609b)

`Transcription App` è una soluzione versatile per la conversione tra audio e testo, supportata da potenti servizi cloud di Azure Cognitive Services. Con un'interfaccia moderna e funzionalità avanzate, questa applicazione permette di trascrivere l’audio in testo e di generare audio da testo scritto, ideale per chiunque desideri strumenti rapidi e accurati per lavorare con contenuti vocali.

## ✨ Funzionalità principali
- **Conversione Audio-Testo**: Carica un file audio o registra direttamente tramite il microfono per ottenere una trascrizione accurata in diverse lingue.
- **Generazione Testo-Audio**: Digita il testo da convertire in audio e ottieni un file scaricabile, con voce sintetizzata di alta qualità.
- **Supporto Multi-lingua**: Seleziona tra diverse lingue supportate per la trascrizione e sintesi, grazie ai servizi di riconoscimento vocale e generazione vocale di Azure.
- **Tecnologia Cloud-Powered**: Utilizza Azure Cognitive Services per ottenere performance avanzate e precisione nel riconoscimento vocale e nella sintesi audio.

## 💻 Ambiente di sviluppo consigliato
Consigliamo l'uso di [Visual Studio Code](https://code.visualstudio.com/) con l’estensione [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) per una migliore esperienza di sviluppo. Disattiva l’estensione Vetur per evitare conflitti.

## 🚀 Setup del progetto

### Prerequisiti
Assicurati di avere [Node.js](https://nodejs.org/) e [Python](https://www.python.org/) installati sul sistema.

### Installazione delle dipendenze

1. **Clona il repository**:

   ```sh
   git clone https://github.com/yourusername/transcription-app.git
   ```

2. **Installa le dipendenze del frontend**:

   ```sh
   cd transcription-app/frontend
   npm install
   ```

3. **Installa le dipendenze del backend**:

   ```sh
   cd ../backend
   pip install -r requirements.txt
   ```

### Avvio del Backend (Flask)

1. **Vai nella cartella del backend**:

   ```sh
   cd transcription-app/backend
   ```

2. **Configura le credenziali di Azure** (aggiungi `AZURE_SPEECH_KEY` e `AZURE_REGION` nel tuo ambiente o in un file `.env`):

   ```plaintext
   AZURE_SPEECH_KEY=your_azure_speech_key
   AZURE_REGION=your_azure_region
   ```

3. **Avvia il server Flask**:

   ```sh
   python app.py
   ```

   Il backend sarà ora attivo su `http://127.0.0.1:5000`.

### Avvio del Frontend (Vue + Vite)

1. **Apri un nuovo terminale** e vai nella cartella `frontend`:

   ```sh
   cd transcription-app/frontend
   ```

2. **Avvia il server di sviluppo Vite**:

   ```sh
   npm run dev
   ```

   Il frontend sarà disponibile su `http://localhost:5173` o una porta simile, indicata nel terminale.

---

## 🗂️ Struttura del progetto

- **frontend/**: Contiene il codice Vue 3 dell'applicazione.
- **backend/**: Modulo backend in Flask per gestire API e logica lato server.
- **node_modules/**: Dipendenze del progetto frontend.
- **dist/**: Directory di output generata per la distribuzione del frontend.

---

## 📝 Configurazione di Azure Cognitive Services

Per usare le funzionalità di trascrizione e sintesi, è necessario configurare le credenziali di Azure. Aggiungi le seguenti variabili nel tuo ambiente o in un file `.env`:

```plaintext
AZURE_SPEECH_KEY=your_azure_speech_key
AZURE_REGION=your_azure_region
```

Puoi ottenere queste informazioni dalla tua dashboard Azure, nella sezione Cognitive Services.

---

## 📋 Riepilogo dei comandi

1. **Backend**:
   - `cd transcription-app/backend`
   - `pip install -r requirements.txt`
   - `python app.py`

2. **Frontend**:
   - `cd transcription-app/frontend`
   - `npm install`
   - `npm run dev`

---

## 📄 License

Questo progetto è rilasciato sotto la licenza MIT.

