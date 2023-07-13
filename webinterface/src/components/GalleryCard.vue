<template>
<div class="GalleryCard">
    <div v-if="!selected" class="gallery">
        <ImageCard v-for="(res, idx) in props.results" 
            :img="res.img" 
            :name="res.name" 
            :key="idx" 
            class="card"
            @click="selected = res"
            />
    </div>
    <div v-else class="zoom">
        <img :src="selected.img" alt="selected image"/>
        <div class="description">
            <h2>{{ selected.name }}</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolor temporibus asperiores, mollitia possimus laudantium sint, provident aliquam alias deleniti dicta sapiente in atque est nesciunt minima quo ut odio error.</p>
            <div>

                <ul v-if="selected.attributes">
                    <li v-for="(value, attr) in selected.attributes" :key="attr"><strong>{{ attr }}</strong>: {{ value }}</li>
                </ul>
                <RadialProgress :value="selected.score"/>
            </div>
            <button @click="selected=undefined">X</button>
        </div>
    </div>
</div>
</template>

<script setup lang="ts">
import { defineProps, ref } from 'vue';
import ImageCard from './ImageCard.vue';
import RadialProgress from './RadialProgress.vue';
import {Result} from './../funcs/types'
const props = defineProps<{
    results : Result[]
}>()

const selected = ref<Result>()

</script>

<style scoped>

.description button {
    position: fixed;
    top: 18vh;
    right: 2em;
}
.description div {
    align-self: center;
}

.zoom .description {
    padding-right: 5em;
    padding-left: 5em;
    display: flex;
    text-align: left;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    
}

.zoom img {
    max-width: 100%;
    max-height: 100%;
    border-radius: 3rem;
    /* max-width: inherit;
    max-height: inherit; */
    object-fit: contain;
}

.zoom {
    height: 84vh;
    display: grid;
    gap: 2em;
    padding: 0 2em;
    align-items: center;
    grid-template-columns: 40% 60%;
}
.card {
    max-height: 30vh;
    max-width: 100%;
}
.gallery {
    display: flex;
    flex-flow: row wrap;
    align-content: flex-start;
    align-items: stretch;
    justify-content: flex-start;
    gap: 1em
}
</style>