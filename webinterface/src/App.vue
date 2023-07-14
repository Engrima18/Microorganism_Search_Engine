<template>
  <div id="root" :class="queried? 'panelshow' : 'covershow'">
    <div id="cover">
        <img v-if="!query" src="./assets/log.png" class="logo">
        <h1>Microorganisms Search Engine</h1>
        <SearchBar v-if="!queried" v-model="query"/>
        <img v-else :src="(query) => to_URL(query)" alt="uploaded image">
        <button v-if="query && !queried" role="button" @click="similarityRequest">Search</button>
        <button v-if="query && queried" role="button" @click="newSearch">New Search</button>
    </div>

    <p>{{ comp_response }}</p>

    <div v-if="queried" id="panels">
      <GalleryCard :results="results"/>
    </div>

  </div>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import SearchBar from './components/SearchBar.vue';
import GalleryCard from './components/GalleryCard.vue';
import { Result } from './funcs/types';
import { convertBase64 } from './funcs/base64'
const query = ref<File>()
const queried = ref<boolean>(false)
const results = ref<Result[]>([])

const comp_response = ref()

async function similarityRequest(e : Event) {
    queried.value=true

    console.log('sent')
    let img_base64 :string = await convertBase64(query.value!)
    console.log(img_base64)

    let response = await fetch('https://0ky1r083ji.execute-api.us-east-1.amazonaws.com/default/black_and_white', {
      method: "POST",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      // make sure to serialize your JSON body
      body: JSON.stringify({
        image: img_base64
      })
    })

    console.log(response)
    comp_response.value = response

    // let res : Result = {
    //   img : query.value,
    //   name : 'bob',
    //   attributes : {'bello': 10, 'specie': 'tua mamma'},
    //   score: 0.7
    // }
    // for (let i=0; i<20; i++) {
    //   results.value.push(res)
    // }

//     import cv2
// import json

// def lambda_handler(event, context):
//     try:
//         image = event['body']['image']
//     except:
//         print('ABORT no parameter image ')
//         return {
//             'statusCode': 200,
//             'body': 'ABORTED, no image' 
//         }
    
//     img = cv2.imread(image)
        
//     print(event)
//     return {
//         'statusCode': 200,
//         'body': json.dumps('yooo')
//     }
    

}

function to_URL(file : File) : string {
  return URL.createObjectURL(file)
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

#root.panelshow {
  margin-top: 16vh;
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
  padding-right: 3vw;
  padding-bottom: 3vh;
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
#root.covershow > #cover h1 {
  flex-grow: 0;
}
h1 {
  margin:0;
  flex-grow: 100;
}

#root.panelshow > #cover {
  height: 10vh;
  flex-direction: row;
  justify-content: flex-end;
  position: fixed;
  top: 0;
  background: white;
  z-index: 2;
  gap: 1em;

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

#cover>.logo {
  max-height: 5em;
  max-width: 5em;
  aspect-ratio: 1/1;
}
</style>
