<template>
  <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      class="arrow-right-icon sm"
      :class="isDisabled ? 'disabled' : ''"
      :style="color ? `stroke: ${color}` : ''"
  >
    <path
        d="M6 12H18M18 12L13 7M18 12L13 17"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
    />
  </svg>
</template>

<script setup>
import { defineProps, defineComponent } from 'vue';

defineComponent({
  name: "ArrowRightIcon",
})

defineProps({
  color: String,
  isDisabled: {type: Boolean, default: false},
})
</script>

<style scoped>
.arrow-right-icon {
  stroke: white;
}

.sm {
  width: 1.5em;
  height: 1.5em;
}

:not(.disabled).arrow-right-icon:hover {
  cursor: pointer;
}
</style>
