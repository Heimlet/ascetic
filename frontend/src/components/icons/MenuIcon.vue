<template>
  <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      class="menu-icon sm"
  >
    <path
        d="M4 6H20M4 12H20M4 18H20"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
    />
  </svg>
</template>

<script setup>
import {defineComponent} from "vue";

defineComponent({
  name: 'MenuIcon',
});
</script>

<style scoped>
.menu-icon {
  stroke: black;
}

.sm {
  width: 1.5em;
  height: 1.5em;
}

.menu-icon:hover {
  cursor: pointer;
}
</style>
