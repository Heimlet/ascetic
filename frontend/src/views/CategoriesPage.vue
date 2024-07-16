<template>
  <div class="categories-page">
    <div class="flex-item">
      <ProductList v-if="category" :category="category" />
    </div>
  </div>
</template>

<script>
import {defineComponent, onBeforeMount, onMounted, ref, watch} from 'vue';
import ProductList from '../components/ProductList.vue';
import { useRoute, useRouter } from 'vue-router';
import { fetchCategories } from "@/services/api.js";

export default defineComponent({
  name: 'CategoriesPage',
  components: {
    ProductList
  },
  props: {
    category: {type: String, default: 'all'}
  },
  setup(props) {
    const route = useRoute();
    const router = useRouter();
    const category = ref(null);
    const categoryCodes = ref([]);

    onBeforeMount(async () => {
      try {
        const categories = await fetchCategories();
        categoryCodes.value = categories.map(item => item.code);

        if (categoryCodes.value.includes(route.params.category)) {
          category.value = route.params.category;
        } else {
          category.value = 'all';
          updateUrl('all');
        }
      } catch (error) {
        console.error('Error fetching categories:', error);
        category.value = 'all';
        updateUrl('all');
      }
    });

    watch(() => props.category, async () => {
      console.log('CategoriesPage watch props.category')
      category.value = props.category;
    });

    const updateUrl = (newCategory) => {
      if (route.params.category !== newCategory) {
        router.replace({ name: route.name, params: { ...route.params, category: newCategory } });
      }
    };

    return {
      category,
    };
  }
});
</script>

<style scoped>
.categories-page {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
