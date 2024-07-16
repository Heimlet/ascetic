<template>
  <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      class="arrow-left-icon sm"
      :class="isDisabled ? 'disabled' : ''"
      :style="color ? `stroke: ${color}` : ''"
  >
    <path
        d="M6 12H18M6 12L11 7M6 12L11 17"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
    />
  </svg>
</template>

<script setup>
import { defineProps, defineComponent } from 'vue';

defineComponent({
  name: 'ArrowLeftIcon'
});

defineProps({
  color: String,
  isDisabled: {type: Boolean, default: false},
})
</script>

<style scoped>
.arrow-left-icon {
  stroke: white;
}

.sm {
  width: 1.5em;
  height: 1.5em;
}

:not(.disabled).arrow-left-icon:hover {
  cursor: pointer;
}
</style>
