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
const showHistory = ref(false)

// Cronologia delle trascrizioni
const transcriptionHistory = ref<Array<{
  id: number,
  filename: string,
  text: string,
  date: string,
  language: string
}>>([])

// Lista delle lingue supportate
const languages = [
  { code: 'it-IT', name: 'Italiano' },
  { code: 'en-US', name: 'English (US)' },
  { code: 'es-ES', name: 'Español' },
  { code: 'fr-FR', name: 'Français' },
  { code: 'de-DE', name: 'Deutsch' }
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
  
  // Salva il file
  const element = document.createElement('a')
  const file = new Blob([transcribedText.value], {type: 'text/plain'})
  element.href = URL.createObjectURL(file)
  element.download = `transcription_${uploadedFileName.value || 'recording'}_${Date.now()}.txt`
  document.body.appendChild(element)
  element.click()
  document.body.removeChild(element)
  
  // Aggiungi alla cronologia
  transcriptionHistory.value.push({
    id: Date.now(),
    filename: uploadedFileName.value || 'Registrazione microfono',
    text: transcribedText.value,
    date: new Date().toLocaleString(),
    language: selectedLanguage.value
  })
  
  statusMessage.value = 'Trascrizione salvata con successo!'
}

const clearHistory = () => {
  transcriptionHistory.value = []
  statusMessage.value = 'Cronologia cancellata'
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
    const audio = new Audio(audioUrl)
    await audio.play()
    statusMessage.value = 'Audio generato con successo!'
  } catch (error) {
    console.error('Error:', error)
    statusMessage.value = 'Errore durante la generazione audio. Riprova.'
  } finally {
    isProcessing.value = false
  }
}
</script>

<template>
  <main class="min-h-screen bg-light-pattern dark:bg-dark-pattern transition-colors duration-300 flex items-center justify-center">
    <div class="max-w-5xl w-full mx-auto px-4 py-12 grid grid-cols-1 md:grid-cols-2 gap-12">
      <!-- Speech to Text (Sinistra) -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-10 transition-all duration-300 hover:shadow-xl">
        <h2 class="text-3xl font-semibold mb-6 text-gray-800 dark:text-white">Speech to Text</h2>

        <!-- Language Selection -->
        <div class="mb-6">
          <label class="block text-sm font-medium text-gray-600 dark:text-gray-300 mb-2">Select Language</label>
          <select 
            v-model="selectedLanguage"
            class="w-full p-3 border rounded-lg bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100">
            <option v-for="lang in languages" :key="lang.code" :value="lang.code">
              {{ lang.name }}
            </option>
          </select>
        </div>

        <!-- Mic Recording -->
        <div class="mb-6">
          <button 
            @click="toggleRecording"
            :disabled="isProcessing"
            :class="{
              'bg-red-500 hover:bg-red-600': isRecording,
              'bg-blue-500 hover:bg-blue-600': !isRecording,
              'opacity-50 cursor-not-allowed': isProcessing
            }"
            class="w-full px-6 py-3 text-white font-medium rounded-lg transition-colors">
            {{ isRecording ? 'Stop Recording' : 'Start Recording' }}
          </button>
        </div>

        <!-- File Upload -->
        <div class="mb-6">
          <div class="flex flex-col items-center">
            <label class="block w-full text-sm font-medium text-gray-600 dark:text-gray-300 mb-2 text-center">
              Choose an audio file
            </label>
            <input 
              type="file" 
              @change="handleFileUpload"
              accept="audio/*"
              class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:font-medium file:bg-blue-100 file:text-blue-700 hover:file:bg-blue-200 dark:file:bg-gray-700 dark:file:text-gray-200 dark:hover:file:bg-gray-600">
          </div>
          <button 
            @click="transcribeFile"
            :disabled="isProcessing || !uploadedFile"
            :class="{
              'opacity-50 cursor-not-allowed': isProcessing || !uploadedFile
            }"
            class="bg-blue-500 hover:bg-blue-600 w-full mt-4 py-3 text-white font-medium rounded-lg transition-colors">
            Transcribe File
          </button>
          <p v-if="uploadedFileName" class="text-sm text-center mt-4 text-gray-600 dark:text-gray-400">
            File selezionato: {{ uploadedFileName }}
          </p>
        </div>

        <!-- Transcription Result -->
        <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg mt-6 text-center">
          <p class="text-gray-600 dark:text-gray-300">
            {{ transcribedText || 'Start recording or upload a file to see transcription...' }}
          </p>
        </div>
      </div>

      <!-- Text to Speech (Destra) -->
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-10 transition-all duration-300 hover:shadow-xl">
        <h2 class="text-3xl font-semibold mb-6 text-gray-800 dark:text-white">Text to Speech</h2>
        <textarea 
          v-model="textToSpeak"
          class="w-full p-3 border rounded-lg mb-6 bg-gray-50 dark:bg-gray-700 text-gray-900 dark:text-gray-100"
          rows="6"
          :disabled="isProcessing"
          placeholder="Enter text to convert to speech...">
        </textarea>
        <button 
          @click="synthesizeSpeech"
          :disabled="isProcessing || !textToSpeak"
          :class="{
            'opacity-50 cursor-not-allowed': isProcessing || !textToSpeak
          }"
          class="bg-green-500 hover:bg-green-600 w-full py-3 text-white font-medium rounded-lg transition-colors">
          Generate Speech
        </button>
      </div>
    </div>
  </main>
</template>

<style scoped>
/* Minimal Apple-inspired styles */
.bg-light-pattern {
  background: #f5f5f7;
}

.bg-dark-pattern {
  background: #1c1c1e;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

.shadow-lg {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.hover\:shadow-xl:hover {
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.15);
}

.rounded-lg {
  border-radius: 16px;
}

button {
  font-weight: 500;
  transition: background-color 0.3s, transform 0.2s;
}

button:active {
  transform: scale(0.98);
}
</style>


