<template>

<label for="images" class="drop-container" id="dropcontainer">
    <div v-if="image" id="preview">
        <img :src="image" alt="uploaded image"/>
    </div>
    <div v-else>
        <span class="drop-title">Drop files here</span>
        <br>
        or
    </div>

    <input 
        type="file" 
        name="image" 
        accept="image/*" 
        required
        @change="showFilePreview"
        >
</label>

<button v-if="image" role="button" @click="sendPhoto">Search</button>

</template>

<script setup lang="ts">
import { ref} from "vue";
const image = ref()

function showFilePreview(e : Event){
    let files = e.target.files || e.dataTransfer.files;
    if (!files.length) return;
    image.value = URL.createObjectURL(files[0]);
}

function sendPhoto(e : Event) {
    
}

</script>

<style>

img {
    max-width: 90%;
    max-height: 90%;
}
.drop-container {
  position: relative;
  display: flex;
  gap: 10px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: max-content;
  padding: 20px;
  border-radius: 10px;
  border: 2px dashed #555;
  color: #444;
  cursor: pointer;
  transition: background .2s ease-in-out, border .2s ease-in-out;
}

.drop-container:hover {
  background: #eee;
  border-color: #111;
}

.drop-container:hover .drop-title {
  color: #222;
}

.drop-title {
  color: #444;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  transition: color .2s ease-in-out;
}


button, input[type=file]::file-selector-button:hover {
  background: #1aa50d;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity .5s
}

.fade-enter,
.fade-leave-to {
    opacity: 0
}

button , input[type=file]::file-selector-button{
    transition: all .2s ease-in-out;

    margin: 1em;
  background: #5E5DF0;
  border-radius: 999px;
  box-shadow: #5E5DF0 0 10px 20px -10px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  font-family: Inter,Helvetica,"Apple Color Emoji","Segoe UI Emoji",NotoColorEmoji,"Noto Color Emoji","Segoe UI Symbol","Android Emoji",EmojiSymbols,-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans",sans-serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 24px;
  opacity: 1;
  outline: 0 solid transparent;
  padding: 8px 18px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  width: fit-content;
  word-break: break-word;
  border: 0;
}
</style>