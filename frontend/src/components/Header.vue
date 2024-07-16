<template>
  <div class="home-container">
    <div class="container">
      <div class="grid-container">
        <div v-for="(category, index) in displayedCategories" :key="category.id" :class="`featured ${gridClasses[index]}`">
          <router-link :to="`categories/${category.code}`">
            <div :id="`img${index + 1}`" class="lil-overlay"></div>
            <img :src="category.image" :alt="category.name"/>
            <p class="main-description">{{ category.name }}</p>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, onMounted, ref, computed } from "vue";
import { fetchCategories } from "@/services/api.js";

export default defineComponent({
  name: 'Header',
  setup() {
    const categories = ref([]);
    const gridClasses = ['grid-one', 'grid-two', 'grid-four', 'grid-four-low'];

    onMounted(async () => {
      categories.value = await fetchCategories(true);
    });

    const displayedCategories = computed(() => {
      return categories.value.slice(0, 4);
    });

    return {
      categories,
      gridClasses,
      displayedCategories,
    };
  },
});
</script>

<style scoped>
.grid-container {
  display: grid;
  height: 50rem;
  grid-template-columns: 2fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  grid-template-areas: 'one two four' 'one two four-low';
  gap: 1.3rem;
  margin-top: 1.3rem;
}

.home-container {
}

.featured {
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.main-description {
  position: absolute;
  bottom: 2rem;
  left: 2rem;
  color: white;
  font-size: 3.8rem;
  font-weight: 600;
}

.featured img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: 50% 50%;
}

.grid-one {
  grid-area: one;
}

.grid-two {
  grid-area: two;
}

.grid-four {
  grid-area: four;
}

.grid-four-low {
  grid-area: four-low;
}

.lil-overlay {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease-in;
}

#img1:hover {
  background-color: rgba(0, 0, 0, 0.5) !important;
}

#img2:hover {
  background-color: rgba(0, 0, 0, 0.5) !important;
}

#img3:hover {
  background-color: rgba(0, 0, 0, 0.5) !important;
}

#img4:hover {
  background-color: rgba(0, 0, 0, 0.5) !important;
}

@media (max-width: 750px) {
  .grid-container {
    height: 500px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-template-areas: "one two" "four four-low";
    grid-gap: 13px;
    gap: 13px;
  }
}

@media (max-width: 450px) {
  .main-description {
    bottom: 1rem;
    left: 1rem;
    font-size: 3rem;
  }
}

@media (max-width: 400px) {
  .main-description {
    bottom: 1rem;
    left: 0.5rem;
    font-size: 2.5rem;
  }
}
</style>
