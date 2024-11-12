# 🎙️ Transcription App

![image](https://github.com/user-attachments/assets/92112801-2b04-429a-b43c-2a2a4d0f609b)


`transcription-app` è una landing page sviluppata in Vue 3 e Vite. Questo progetto offre una base per costruire applicazioni moderne, ottimizzate per prestazioni e sviluppo rapido, sfruttando strumenti e tecnologie come TypeScript, ESLint e una configurazione iniziale per facilitare lo sviluppo.

## ✨ Funzionalità principali
- **Framework**: Vue 3 con TypeScript, che permette uno sviluppo modulare e mantenibile.
- **Bundler**: Vite, per un'esperienza di sviluppo veloce grazie al server di sviluppo ad alte prestazioni e alla possibilità di usare Hot Module Replacement (HMR).
- **Linting**: ESLint, per mantenere uno stile di codice coerente e individuare errori in fase di sviluppo.

## 💻 Ambiente di sviluppo consigliato
Si consiglia l'uso di [Visual Studio Code](https://code.visualstudio.com/) con l'estensione [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) abilitata (e con l’estensione Vetur disabilitata) per una migliore esperienza di sviluppo in Vue.

## 📂 Supporto TypeScript per importazioni `.vue`
Poiché TypeScript non supporta nativamente i file `.vue`, è consigliato usare `vue-tsc` per il controllo dei tipi. [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) è richiesto per integrare correttamente il servizio di TypeScript.

## ⚙️ Configurazione personalizzata
Consulta la [documentazione di Vite](https://vite.dev/config/) per maggiori dettagli sulla configurazione.

## 🚀 Setup del progetto

### Installazione delle dipendenze

Assicurati di avere [Node.js](https://nodejs.org/) installato. Poi esegui:

```sh
npm install
```

### Compilazione e hot-reload per lo sviluppo

```sh
npm run dev
```

### Controllo dei tipi, compilazione e minificazione per la produzione

```sh
npm run build
```

### Lint del codice con [ESLint](https://eslint.org/)

```sh
npm run lint
```

## 🗂️ Struttura del progetto

- **frontend/**: Contiene il codice Vue 3 dell'applicazione.
- **backend/**: Modulo backend (se presente) per gestire API o logica lato server (opzionale).
- **node_modules/**: Dipendenze del progetto (escluse dal repository grazie a `.gitignore`).
- **dist/**: Directory di output generata per la distribuzione.

---

Questa struttura e configurazione rendono il progetto pronto per la scalabilità e facile da mantenere nel tempo.
Ecco i comandi ordinati per avviare correttamente la tua applicazione **Transcription App** sia per il backend (Flask) che per il frontend (Vue + Vite).

---

## 🎙️ Transcription App - Guida all'avvio

### **1. Avvio del Backend (Flask)**

1. **Apri il terminale** e vai nella cartella `backend`:
   ```sh
   cd transcription-app/backend
   ```

2. **Installa le dipendenze**:
   ```sh
   pip install -r requirements.txt
   ```
   *Se `requirements.txt` non è presente, installa manualmente i pacchetti come `flask`, `azure-cognitiveservices-speech`, e `pydub` con `pip install nome_pacchetto`.*

3. **Avvia il server Flask**:
   ```sh
   python app.py
   ```

   Il backend sarà ora attivo su `http://127.0.0.1:5000`.

### **2. Avvio del Frontend (Vue + Vite)**

1. **Apri un nuovo terminale** e vai nella cartella `frontend/transcription-app`:
   ```sh
   cd transcription-app/frontend/transcription-app
   ```

2. **Installa le dipendenze**:
   ```sh
   npm install
   ```

3. **Avvia il server di sviluppo Vite**:
   ```sh
   npm run dev
   ```

   Il frontend sarà disponibile su `http://localhost:5173` o una porta simile (indicata nel terminale).

---

### **Riepilogo dei comandi**

1. **Backend**:
   - `cd transcription-app/backend`
   - `pip install -r requirements.txt`
   - `python app.py`

2. **Frontend**:
   - `cd transcription-app/frontend/transcription-app`
   - `npm install`
   - `npm run dev`


