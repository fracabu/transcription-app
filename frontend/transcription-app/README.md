# 🎙️ Transcription App

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
