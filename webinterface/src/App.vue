<template>
  <div id="root">
    <SearchBar v-model="image"/>
    <button v-if="image" role="button" @click="sendPhoto">Search</button>

  </div>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import SearchBar from './components/SearchBar.vue';
const image = ref<string | undefined>(undefined)

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
