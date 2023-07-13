<template>
  <div id="root" :class="queried? 'panelshow' : 'covershow'">
    <div id="cover">
        <h1>Microorganisms Search Engine</h1>
        <SearchBar v-if="!queried" v-model="query"/>
        <img v-else :src="query" alt="uploaded image">
        <button v-if="query && !queried" role="button" @click="similarityRequest">Search</button>
        <button v-if="query && queried" role="button" @click="newSearch">X</button>
    </div>

    <div v-if="queried" id="panels">
      <GalleryCard :images="results"/>
    </div>

  </div>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import SearchBar from './components/SearchBar.vue';
import ImageCard from './components/ImageCard.vue';
import GalleryCard from './components/GalleryCard.vue';
const query = ref<string | undefined>(undefined)
const queried = ref<boolean>(false)
const results = ref<string[]>([])

function similarityRequest(e : Event) {
    console.log(query)
    queried.value=true
    for (let i=0; i<20; i++) {
      results.value.push(query.value)
    }
}

function newSearch(e: Event) {
  queried.value = false
  query.value = undefined
  results.value = []
}

</script>

<style>
#root {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

#root.covershow > #panels {
  display: none;
}

#root > #cover {
  width: 94vw;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  height: inherit;
  padding-left: 3vw;
  padding-top: 3vh;
}

#cover>img {
  transition: all 0 ease;
  max-height: inherit;
  object-fit: cover;
  height: inherit;
  border-radius: 1rem;
}

#root.covershow > #cover {
  height: 94vh;
  flex-direction: column;
  
}

#root.panelshow > #cover {
  height: 10vh;
  flex-direction: row;
}

#cover {
  transition: all 0.3s ease;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body{
  margin:0;
}

button , input[type=file]::file-selector-button{
    transition: all .2s ease-in-out;
    margin: 0.3em;
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
  white-space: nowrap;
}
button:hover, input[type=file]::file-selector-button:hover {
  background: #1aa50d;
}
h1 {
  margin:0;
}
</style>
