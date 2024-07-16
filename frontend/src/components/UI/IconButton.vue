<template>
  <button
      :class="{ button: true, disabled: isDisabled}"
      @click="handleClick"
      :disabled="isDisabled">
    <slot name="icon"/>
  </button>
</template>

<script>
import {defineComponent, toRefs} from "vue";

export default defineComponent({
  name: "IconButton",
  props: {
   isDisabled: {
      type: Boolean,
      default: false,
    },
    onClick: {
      type: Function,
      required: true,
    },
  },
  setup(props) {
    const { isDisabled, onClick } = toRefs(props);

    const handleClick = () => {
      if (!isDisabled.value) {
        onClick.value();
      }
    };

    return {
      isDisabled,
      handleClick,
    }
  }

})
</script>

<style scoped>
button {
  color: white;
  background-color: #373737;
  padding: 1rem;
  font-size: 1.5rem;
  border: none;
  height: 4rem;
  width: 4rem;
  cursor: pointer;
  transition: all 0.1s ease-in;
}

.disabled {
  background-color: #444444;
  cursor: not-allowed;
}

button:not(.disabled):hover {
  background-color: black;
}
</style>