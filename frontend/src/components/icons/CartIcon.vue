<template>
  <div class="cart-icon-container">
    <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        class="cart-icon"
        :class="size === 'large' ? 'cart-icon-lg' : ''"
    >
      <path d="M6.29977 5H21L19 12H7.37671M20 16H8L6 3H3M9 20C9 20.5523 8.55228 21 8 21C7.44772 21 7 20.5523 7 20C7 19.4477 7.44772 19 8 19C8.55228 19 9 19.4477 9 20ZM20 20C20 20.5523 19.5523 21 19 21C18.4477 21 18 20.5523 18 20C18 19.4477 18.4477 19 19 19C19.5523 19 20 19.4477 20 20Z"/>
    </svg>
    <span v-if="count > 0"
          class="cart-badge"
          :class="size === 'large' ? 'cart-badge-lg' : ''"
    >{{ count }}</span>
  </div>
</template>

<script setup>
import { defineProps, defineComponent } from 'vue';

defineComponent({
  name: 'CartIcon',
})

defineProps({
  count: {
    type: Number,
    default: 9,
  },
  size: {
    type: String,
    default: '',
  }
})
</script>

<style scoped>
.cart-icon-container {
  position: relative;
  display: inline-block;
}

.cart-icon {
  width: 1em;
  height: 1em;
  color: currentColor;
}


.cart-icon-lg {
  width: 1.5em;
  height: 1.5em;
}

.cart-badge {
  position: absolute;
  top: -0.5em;
  right: -0.5em;
  background-color: #b6002c;
  color: white;
  border-radius: 50%;
  padding: 0.2em 0.4em;
  font-size: 0.5em;
  text-decoration: none;
  font-style: normal;
}

.cart-badge-lg {
  font-size: 0.75em;
}

</style>
