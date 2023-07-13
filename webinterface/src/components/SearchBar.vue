<template>

<label for="images" class="drop-container" id="dropcontainer">
    <div v-if="props.modelValue" id="preview">
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


</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref } from "vue";
const props = defineProps({
  modelValue : String
})

const emit = defineEmits(['update:modelValue'])

const image = ref<string>()
function showFilePreview(e : Event){
    let files = e.target?.files || e.dataTransfer.files;
    if (!files.length) return;
    image.value = URL.createObjectURL(files[0]);
    emit('update:modelValue', image.value)
}
</script>

<style scoped>

img {
  max-height : 60vh;
  max-width: 60vw;
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
  overflow: hidden;
  max-height: 90vh;
  object-fit: cover;
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

.fade-enter-active,
.fade-leave-active {
    transition: opacity .5s
}

.fade-enter,
.fade-leave-to {
    opacity: 0
}

</style>