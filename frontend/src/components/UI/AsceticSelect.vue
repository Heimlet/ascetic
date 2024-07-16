<template>
  <div class="ascetic-select" @click="toggleDropdown" v-click-outside="closeDropdown">
    <div class="selected-option">
      {{ selectedOption ? selectedOption.name : 'Select an option' }}
      <div class="select-arrow"></div>
    </div>
    <div v-if="dropdownOpen" class="dropdown-options">
      <div
          v-for="option in options"
          :key="option.value"
          class="dropdown-option"
          @click="selectOption(option)"
      >
        {{ option.name }}
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';

export default defineComponent({
  name: 'AsceticSelect',
  props: {
    options: {
      type: Array,
      required: true,
      validator(value) {
        return value.every(option => 'value' in option && 'name' in option);
      }
    },
    onChange: {
      type: Function,
      required: true,
    },
    defaultOption: {
      type: Object,
      default: null,
      validator(value) {
        return value === null || ('value' in value && 'name' in value);
      }
    }
  },
  setup(props) {
    const selectedOption = ref(props.defaultOption || null);
    const dropdownOpen = ref(false);

    const toggleDropdown = () => {
      dropdownOpen.value = !dropdownOpen.value;
    };

    const closeDropdown = () => {
      dropdownOpen.value = false;
    };

    const selectOption = (option) => {
      selectedOption.value = option;
      dropdownOpen.value = false;
      props.onChange(option.value);
    };

    onMounted(() => {
      if (props.defaultOption) {
        const exists = props.options.some(option => option.value === props.defaultOption.value);
        if (!exists) {
          console.warn(`Default option with value '${props.defaultOption.value}' does not exist in options array.`);
        }
      }
    });

    return {
      selectedOption,
      dropdownOpen,
      toggleDropdown,
      selectOption,
      closeDropdown,
    };
  }
});
</script>

<style scoped>
.ascetic-select {
  position: relative;
  width: 100%;
  max-width: 300px;
  user-select: none;
  font-size: 1.4rem;
}

.selected-option {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border: 3px solid rgba(0, 0, 0, 0.3);
  cursor: pointer;
}

.select-arrow {
  width: 1rem;
  height: 1rem;
  background-color: black;
  clip-path: polygon(50% 100%, 100% 0%, 0% 0%);
}

.dropdown-options {
  position: absolute;
  width: 100%;
  border: 1px solid #ccc;
  background-color: #fff;
  z-index: 1000;
}

.dropdown-option {
  padding: 1rem;
  cursor: pointer;
}

.dropdown-option:hover {
  background-color: #f1f1f1;
}
</style>
