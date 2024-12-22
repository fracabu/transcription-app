
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

Ecco la sezione aggiornata con il comando per attivare l'ambiente virtuale del backend prima di avviare il server Flask:

---

## 🚀 Setup del progetto

### **1. Avvio del Backend (Flask)**

1. **Apri il terminale** e vai nella cartella `backend`:
   ```sh
   cd transcription-app/backend
   ```

2. **Attiva l'ambiente virtuale**:
   Se hai già configurato un ambiente virtuale (ad esempio `venv`), attivalo con il comando corretto:

   - **Su Windows**:
     ```sh
     venv\Scripts\activate
     ```
   - **Su Linux/Mac**:
     ```sh
     source venv/bin/activate
     ```

3. **Installa le dipendenze**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Configura le credenziali di Azure**:  
   Assicurati di aggiungere le seguenti variabili nel tuo ambiente o in un file `.env`:
   ```plaintext
   AZURE_SPEECH_KEY=your_azure_speech_key
   AZURE_REGION=your_azure_region
   ```

5. **Avvia il server Flask**:
   ```sh
   python app.py
   ```

   Il backend sarà ora attivo su `http://127.0.0.1:5000`.

---

### **2. Avvio del Frontend (Vue + Vite)**

1. **Apri un nuovo terminale** e vai nella directory del frontend:
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

   Il frontend sarà disponibile su `http://localhost:5173` o una porta simile indicata nel terminale.

---

Ora sei pronto per utilizzare la tua applicazione **Transcription App**!

## 🗂️ Struttura del progetto

- **frontend/**: Contiene il codice Vue 3 dell'applicazione.
- **backend/**: Modulo backend in Flask per gestire API e logica lato server.
- **node_modules/**: Dipendenze del progetto frontend.
- **dist/**: Directory di output generata per la distribuzione del frontend.

---

Questa struttura e configurazione rendono il progetto pronto per la scalabilità e facile da mantenere nel tempo.
Ecco i comandi ordinati per avviare correttamente la tua applicazione **Transcription App** sia per il backend (Flask) che per il frontend (Vue + Vite).

---


### **Riepilogo dei comandi**

Ecco la procedura completa e aggiornata:

**1. Avviare il Backend:**
```bash
# Vai nella directory backend
cd transcription-app/backend

# Attiva l'ambiente virtuale
venv\Scripts\activate

# Installa le dipendenze (se non l'hai già fatto)
pip install -r requirements.txt
pip install python-dotenv

# Avvia il server Flask
python app.py
```
Il backend dovrebbe avviarsi su `http://127.0.0.1:5000`

**2. Avviare il Frontend** (in un nuovo terminale):
```bash
# Vai nella directory frontend
cd transcription-app/frontend

# Installa le dipendenze (se non l'hai già fatto)
npm install

# Avvia il server di sviluppo
npm run dev
```
Il frontend dovrebbe avviarsi su `http://localhost:5173`

Se tutto è andato a buon fine:
- Backend sarà attivo su http://127.0.0.1:5000
- Frontend sarà accessibile su http://localhost:5173
- Dovresti vedere l'interfaccia dell'app di trascrizione nel browser

Ricorda di mantenere entrambi i terminali aperti mentre usi l'applicazione.