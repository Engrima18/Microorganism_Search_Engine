<template>
  <div class="GalleryCard">
    <ImageCard v-for="img in props.images" :img="img" name="bro" :key="img" class="card"/>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';
import ImageCard from './ImageCard.vue';
const props = defineProps({
    images : Object
})
</script>

<style scoped>

.card {
    max-height: 30vh;
    max-width: 100%;
}
.GalleryCard {
    display: flex;
    flex-flow: row wrap;
    align-content: flex-start;
    align-items: stretch;
    justify-content: flex-start;
    gap: 1em
}
</style>