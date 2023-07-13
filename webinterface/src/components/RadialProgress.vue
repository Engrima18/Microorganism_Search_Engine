<template>


<svg
   class="progress-ring"
   width="120"
   height="120">
  <circle
    class="progress-ring__circle"
    :stroke="`rgb(${255*(1-props.value)},${255*props.value},30)`"
    stroke-width="10"
    fill="transparent"
    :style="{'stroke-dashoffset': (1-props.value) *circumference  }"
    :r="radius"
    cx="60"
    cy="60"/>
    <text x="50%" y="50%" font-size="1.5em" text-anchor="middle" dy=".3em">{{props.value * 100}}%</text>
</svg>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';
const radius = 52
const circumference = radius * 2 * Math.PI

const props = defineProps({
    value : Number
})
</script>

<style scoped>
.progress-ring {

}

circle {
    stroke-dasharray: 314 314 ;
}

.progress-ring__circle {
  transition: 0.35s stroke-dashoffset;
  transform: rotate(-90deg);
  transform-origin: 50% 50%;
}

</style>