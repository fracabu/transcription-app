<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const isRecording = ref<boolean>(false)
const transcribedText = ref<string>('') 
const textToSpeak = ref<string>('') 
const selectedLanguage = ref('it-IT') 
const uploadedFile = ref<File | null>(null)
const isProcessing = ref(false)
const statusMessage = ref('')
const uploadedFileName = ref('')

// Lista delle lingue supportate
const languages = [
  { code: 'it-IT', name: 'Italiano' },
  { code: 'en-US', name: 'English (US)' },
  { code: 'es-ES', name: 'Español' },
  { code: 'fr-FR', name: 'Français' },
  { code: 'de-DE', name: 'Deutsch' },
  { code: 'pt-BR', name: 'Português' },
  { code: 'ja-JP', name: '日本語' },
  { code: 'ko-KR', name: '한국어' },
  { code: 'zh-CN', name: '中文' },
  { code: 'ar-SA', name: 'العربية' },
  { code: 'ru-RU', name: 'Русский' },
  { code: 'hi-IN', name: 'हिन्दी' },
  { code: 'tr-TR', name: 'Türkçe' },
  { code: 'nl-NL', name: 'Nederlands' },
  { code: 'pl-PL', name: 'Polski' },
  { code: 'sv-SE', name: 'Svenska' },
  { code: 'da-DK', name: 'Dansk' },
  { code: 'fi-FI', name: 'Suomi' },
  { code: 'no-NO', name: 'Norsk' },
  { code: 'cs-CZ', name: 'Čeština' },
  { code: 'hu-HU', name: 'Magyar' },
  { code: 'ro-RO', name: 'Română' },
  { code: 'el-GR', name: 'Ελληνικά' },
  { code: 'th-TH', name: 'ไทย' },
  { code: 'id-ID', name: 'Bahasa Indonesia' },
  { code: 'ms-MY', name: 'Bahasa Melayu' },
  { code: 'vi-VN', name: 'Tiếng Việt' },
  { code: 'bg-BG', name: 'Български' },
  { code: 'hr-HR', name: 'Hrvatski' },
  { code: 'sr-RS', name: 'Српски' },
  { code: 'uk-UA', name: 'Українська' },
  { code: 'he-IL', name: 'עברית' },
  { code: 'ar-SA', name: 'العربية' },
  { code: 'hi-IN', name: 'हिन्दी' },
  { code: 'tr-TR', name: 'Türkçe' },
  { code: 'nl-NL', name: 'Nederlands' },
  { code: 'pl-PL', name: 'Polski' },
  { code: 'sv-SE', name: 'Svenska' },
  { code: 'da-DK', name: 'Dansk' },
  { code: 'fi-FI', name: 'Suomi' },
  { code: 'no-NO', name: 'Norsk' },
  { code: 'cs-CZ', name: 'Čeština' },
  { code: 'hu-HU', name: 'Magyar' },
  { code: 'ro-RO', name: 'Română' },
  { code: 'el-GR', name: 'Ελληνικά' },
  { code: 'th-TH', name: 'ไทย' },
  { code: 'id-ID', name: 'Bahasa Indonesia' },
  { code: 'ms-MY', name: 'Bahasa Melayu' },
  { code: 'vi-VN', name: 'Tiếng Việt' },
  { code: 'bg-BG', name: 'Български' },
  { code: 'hr-HR', name: 'Hrvatski' },
  { code: 'sr-RS', name: 'Српски' },
  { code: 'uk-UA', name: 'Українська' },
  { code: 'he-IL', name: 'עברית' }
  
]

let mediaRecorder: MediaRecorder | null = null
let audioChunks: Blob[] = []

const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files) {
    uploadedFile.value = target.files[0]
    uploadedFileName.value = target.files[0].name
    statusMessage.value = `File selezionato: ${target.files[0].name}`
  }
}

const saveTranscription = () => {
  if (!transcribedText.value) {
    statusMessage.value = 'Nessun testo da salvare'
    return
  }
  
  const element = document.createElement('a')
  const file = new Blob([transcribedText.value], {type: 'text/plain'})
  element.href = URL.createObjectURL(file)
  element.download = `transcription_${uploadedFileName.value || 'recording'}_${Date.now()}.txt`
  document.body.appendChild(element)
  element.click()
  document.body.removeChild(element)
  
  statusMessage.value = 'Trascrizione salvata con successo!'
}

const transcribeFile = async () => {
  if (!uploadedFile.value) {
    statusMessage.value = 'Per favore seleziona un file audio'
    return
  }

  isProcessing.value = true
  statusMessage.value = 'Trascrizione in corso...'
  const formData = new FormData()
  formData.append('audio', uploadedFile.value)
  formData.append('language', selectedLanguage.value)
  
  try {
    const response = await axios.post('http://localhost:5000/api/transcribe', formData)
    transcribedText.value = response.data.transcription
    statusMessage.value = 'Trascrizione completata con successo!'
  } catch (error) {
    console.error('Error:', error)
    transcribedText.value = ''
    statusMessage.value = 'Errore durante la trascrizione. Riprova.'
  } finally {
    isProcessing.value = false
  }
}

const toggleRecording = async () => {
  try {
    if (!isRecording.value) {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      mediaRecorder = new MediaRecorder(stream)
      audioChunks = []

      mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data)
      }

      mediaRecorder.onstop = async () => {
        isProcessing.value = true
        statusMessage.value = 'Elaborazione della registrazione...'
        const audioBlob = new Blob(audioChunks)
        const formData = new FormData()
        formData.append('audio', audioBlob, 'recording.wav')
        formData.append('language', selectedLanguage.value)
        
        try {
          const response = await axios.post('http://localhost:5000/api/transcribe', formData)
          transcribedText.value = response.data.transcription
          statusMessage.value = 'Trascrizione completata con successo!'
        } catch (error) {
          console.error('Error:', error)
          transcribedText.value = ''
          statusMessage.value = 'Errore durante la trascrizione. Riprova.'
        } finally {
          isProcessing.value = false
        }
      }

      mediaRecorder.start()
      statusMessage.value = 'Registrazione in corso...'
    } else {
      mediaRecorder?.stop()
      statusMessage.value = 'Registrazione terminata. Elaborazione...'
    }
    isRecording.value = !isRecording.value
  } catch (error) {
    console.error('Error accessing microphone:', error)
    statusMessage.value = 'Errore accesso al microfono. Verifica i permessi.'
  }
}

const synthesizeSpeech = async () => {
  if (!textToSpeak.value) {
    statusMessage.value = 'Inserisci del testo da convertire'
    return
  }
  
  isProcessing.value = true
  statusMessage.value = 'Generazione audio in corso...'
  
  try {
    const response = await axios.post('http://localhost:5000/api/synthesize', {
      text: textToSpeak.value,
      language: selectedLanguage.value
    }, {
      responseType: 'blob'
    })
    
    const audioUrl = URL.createObjectURL(response.data)
    const downloadLink = document.createElement('a')
    downloadLink.href = audioUrl
    downloadLink.download = `synthesized_audio_${Date.now()}.wav`
    document.body.appendChild(downloadLink)
    downloadLink.click()
    document.body.removeChild(downloadLink)
    
    statusMessage.value = 'Audio generato e scaricato con successo!'
  } catch (error) {
    console.error('Error:', error)
    statusMessage.value = 'Errore durante la generazione audio. Riprova.'
  } finally {
    isProcessing.value = false
  }
}
</script>

<template>
  <div class="app-container">
    <h1 class="title">Audio to Text - Text to Audio</h1>
    <h3 class="subtitle">powered by Azure</h3>
    <main class="main-container">
      <!-- Speech to Text -->
      <div class="card">
        <h2 class="section-title">Speech to Text</h2>

        <!-- Language Selection -->
        <div class="input-group">
          <label class="label">Select Language</label>
          <select v-model="selectedLanguage" class="input-field">
            <option v-for="lang in languages" :key="lang.code" :value="lang.code">
              {{ lang.name }}
            </option>
          </select>
        </div>

        <!-- Mic Recording -->
        <div class="button-group">
          <button @click="toggleRecording" :disabled="isProcessing" 
                  :class="['record-button', { 'recording': isRecording }]">
            {{ isRecording ? '⏹ Stop Recording' : '🎤 Start Recording' }}
          </button>
        </div>

        <!-- File Upload -->
        <div class="input-group">
          <div class="file-upload-container">
            <input type="file" @change="handleFileUpload" accept="audio/*" class="file-input" id="file-upload">
            <label for="file-upload" class="file-upload-label">
              <span class="upload-icon">📁</span>
              <span class="upload-text">Choose audio file or drag & drop</span>
            </label>
          </div>
          <button @click="transcribeFile" :disabled="isProcessing || !uploadedFile" class="transcribe-button">
            🔄 Transcribe File
          </button>
          <p v-if="uploadedFileName" class="file-name">📎 {{ uploadedFileName }}</p>
        </div>

        <!-- Transcription Result -->
        <div class="input-group">
          <label class="label">Transcription Result</label>
          <textarea v-model="transcribedText" class="textarea" rows="6" placeholder="Transcription will appear here..."></textarea>
          <button v-if="transcribedText" @click="saveTranscription" class="download-button">
            💾 Save Transcription
          </button>
        </div>
      </div>

      <!-- Text to Speech -->
      <div class="card">
        <h2 class="section-title">Text to Speech</h2>
        <div class="input-group">
          <label class="label">Enter Text</label>
          <textarea v-model="textToSpeak" class="textarea" rows="6" 
                    placeholder="Type or paste text here to convert to speech..."></textarea>
          <button @click="synthesizeSpeech" :disabled="isProcessing || !textToSpeak" class="speak-button">
            🔊 Generate Speech
          </button>
        </div>
      </div>
    </main>

    <!-- Status Message -->
    <div v-if="statusMessage" class="status-message" role="alert">
      {{ statusMessage }}
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
/* Import font se non già presente */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap');

:root {
  --background: #111111;
  --card-bg: #1a1a1a;
  --accent: #e61e25;
  --accent-hover: #ff1a1a;
  --accent-dark: #cc0000;
  --text-primary: #ffffff;
  --text-secondary: #e0e0e0;
  --border-color: #2a2a2a;
  --input-bg: #2a2a2a;
}

.app-container {
  min-height: 100vh;
  background-color: var(--background);
  padding: 2rem 1rem;
  color: var(--text-primary);
}

.title {
  color: var(--text-primary);
  text-align: center;
  font-size: 2rem;
  font-weight: normal;
  margin-bottom: 2.5rem;
  font-family: 'Press Start 2P', cursive;
  text-transform: uppercase;
  line-height: 1.5;
}

.section-title {
  color: var(--text-primary);
  font-size: 1.5rem;
  font-weight: normal;
  margin-bottom: 2rem;
  font-family: 'Press Start 2P', cursive;
  line-height: 1.4;
  position: relative;
  padding-left: 1rem;
}

.section-title::before {
  content: '>';
  position: absolute;
  left: -0.5rem;
  color: var(--accent);
  animation: blink 1s step-end infinite;
}

.main-container {
  display: flex;
  justify-content: center;
  align-items: stretch;
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 2rem;
  flex: 1;
  max-width: 500px;
}

.input-group {
  margin-bottom: 1.5rem;
}

.label {
  display: block;
  color: var(--text-secondary);
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

/* Improved Select Styling */
select.input-field {
  width: 100%;
  padding: 0.8rem;
  background-color: var(--input-bg);
  color: var(--text-primary);
  border: 2px solid var(--border-color);
  border-radius: 8px;
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23e61e25' d='M11 3L6 8 1 3z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  background-size: 12px;
  padding-right: 2.5rem;
}

/* 3D Button Style */
.record-button,
.transcribe-button,
.speak-button,
.download-button {
  width: 100%;
  padding: 1rem;
  border: none;
  border-radius: 8px;
  background: linear-gradient(to bottom, #ff4444, #cc0000);
  color: var(--text-primary);
  font-weight: 600;
  cursor: pointer;
  position: relative;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.9rem;
  border-top: 1px solid #ff6666;
  border-bottom: 4px solid #990000;
  text-shadow: 1px 1px #990000;
  transition: all 0.1s ease;
}

.record-button:hover,
.transcribe-button:hover,
.speak-button:hover,
.download-button:hover {
  background: linear-gradient(to bottom, #ff5555, #dd0000);
  transform: translateY(-1px);
}

.record-button:active,
.transcribe-button:active,
.speak-button:active,
.download-button:active {
  transform: translateY(2px);
  border-bottom: 2px solid #990000;
}

.record-button.recording {
  background: linear-gradient(to bottom, #ff6666, #ee0000);
  animation: pulse 2s infinite;
}

/* Improved File Upload */
.file-upload-container {
  position: relative;
  margin-bottom: 1rem;
}

.file-input {
  position: absolute;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
  z-index: 2;
}

.file-upload-label {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background: var(--input-bg);
  border: 2px dashed var(--accent);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.file-upload-label:hover {
  background: rgba(230, 30, 37, 0.1);
  border-color: var(--accent-hover);
}

.upload-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.upload-text {
  color: var(--text-secondary);
  text-align: center;
}

/* Textarea Styling */
.textarea {
  width: 100%;
  min-height: 120px;
  padding: 1rem;
  background-color: var(--input-bg);
  color: var(--text-primary);
  border: 2px solid var(--border-color);
  border-radius: 8px;
  resize: vertical;
  line-height: 1.6;
  font-family: inherit;
}

.textarea:focus {
  border-color: var(--accent);
  outline: none;
}

/* Status Message */
.status-message {
  position: fixed;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(26, 26, 26, 0.95);
  border-left: 4px solid var(--accent);
  padding: 1rem 2rem;
  border-radius: 8px;
  color: var(--text-primary);
  font-size: 0.875rem;
  backdrop-filter: blur(8px);
  animation: fadeIn 0.3s ease;
  z-index: 1000;
}

/* Animations */
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(230, 30, 37, 0.4); }
  70% { box-shadow: 0 0 0 10px rgba(230, 30, 37, 0); }
  100% { box-shadow: 0 0 0 0 rgba(230, 30, 37, 0); }
}

@keyframes blink {
  50% { opacity: 0; }
}

@keyframes fadeIn {
  from { opacity: 0; transform: translate(-50%, 1rem); }
  to { opacity: 1; transform: translate(-50%, 0); }
}

/* Responsive Design */
@media (max-width: 768px) {
  .main-container {
    flex-direction: column;
  }
  
  .title {
    font-size: 1.5rem;
  }
  
  .section-title {
    font-size: 1.25rem;
  }
  
  .card {
    max-width: 100%;
  }
}

/* Disabled States */
button:disabled {
  background: linear-gradient(to bottom, #888888, #666666);
  border-top: 1px solid #999999;
  border-bottom: 4px solid #444444;
  color: #cccccc;
  cursor: not-allowed;
  text-shadow: none;
}



.subtitle {
  display: block;
  color: #ff3333;
  font-size: 24px;
  text-align: center;
  margin-top: -2rem;
  margin-bottom: 3rem;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
  letter-spacing: 0.5px;
  padding: 0.5rem;
  position: relative;
  z-index: 1;
}

/* Variante con gradiente più sottile e leggibile */
.subtitle span {
  background: linear-gradient(to right, #ff3333, #ff4d4d);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Media query per schermi più piccoli */
@media (max-width: 768px) {
  .subtitle {
    font-size: 0.85rem;
    margin-top: -1.5rem;
    margin-bottom: 2rem;
  }
}

/* Fallback per browser che non supportano il gradient text */
@supports not (background-clip: text) {
  .subtitle span {
    color: #ff3333;
    -webkit-text-fill-color: initial;
  }
}
</style>