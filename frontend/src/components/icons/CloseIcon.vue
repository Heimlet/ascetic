<template>
  <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="-0.5 0 25 25"
      fill="none"
      class="close-icon"
  >
    <path
        d="M3 21.32L21 3.32001"
        stroke="#000000"
        stroke-width="1.5"
        stroke-linecap="round"
        stroke-linejoin="round"
    />
    <path
        d="M3 3.32001L21 21.32"
        stroke="#000000"
        stroke-width="1.5"
        stroke-linecap="round"
        stroke-linejoin="round"
    />
  </svg>
</template>

<script setup>
import { defineComponent } from 'vue';

defineComponent({
  name: 'CloseIcon',
});
</script>

<style scoped>
.close-icon {
  width: 1.5em;
  height: 1.5em;
  color: currentColor;
}

.close-icon:hover {
  cursor: pointer;
}
</style>
