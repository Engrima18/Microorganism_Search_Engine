<template>
<div class="ImageCard" @click="emit('click', props.img, props.name, props.infos)">
    <figure>
        <img :src="img" :alt="name">
        <figcaption>{{ name }}</figcaption>
    </figure>
</div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';
const props = defineProps({
    img : String,
    name : String,
    infos : Object
})

const emit = defineEmits(['click'])


</script>

<style scoped>
img {
    max-height: inherit;
  object-fit: cover;
  height: inherit;
}
figure {
  display: grid;
  border-radius: 1rem;
  overflow: hidden;
  cursor: pointer;
  max-height: inherit;
    max-width: inherit;
}
figure > * {
  grid-area: 1/1;
  transition: .4s;
}
figure figcaption {
  display: grid;
  align-items: end;
  font-family: sans-serif;
  font-size: 2.3rem;
  font-weight: bold;
  color: #0000;
  padding: .75rem;
  background: var(--c,#0009);
  clip-path: inset(0 var(--_i,100%) 0 0);
  -webkit-mask:
    linear-gradient(#000 0 0),
    linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  -webkit-mask-clip: text, padding-box;
  margin: -1px;
}
figure:hover figcaption{
  --_i: 0%;
}
figure:hover img {
  transform: scale(1.2);
}
@supports not (-webkit-mask-clip: text) {
  figure figcaption {
   -webkit-mask: none;
   color: #fff;
  }
}

</style>