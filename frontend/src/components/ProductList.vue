<template>
  <div class="container product-list">
    <div class="flex-item product-list-header">
      <div class="filter-btns">
        <button v-for="category in categories" :key="category.code" @click="filterByCategory(category.code)">
          {{ category.name }}
        </button>
        <AsceticSelect
            :on-change="onPerPageChange"
            :options="perPageOptions"
            :defaultOption="perPageOptions.find((el) => el.value === '8')"
            class="perpage-select"
        />
      </div>
    </div>
    <div class="flex-item">
      <ProductsGrid :products="products"/>
    </div>
    <div class="flex-item pagination" v-if="totalPages > 1">
      <div class="paginator-btns">
        <IconButton :on-click="prevPage" :isDisabled="page === 1">
          <template v-slot:icon>
            <ArrowLeftIcon :is-disabled="page === 1"/>
          </template>
        </IconButton>
        <IconButton :on-click="nextPage" :isDisabled="page === totalPages">
          <template v-slot:icon>
            <ArrowRightIcon :is-dsabled="page === totalPages"/>
          </template>
        </IconButton>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, defineComponent, onMounted, ref, watch } from 'vue';
import Product from './Product.vue';
import { fetchProducts, fetchCategories } from '../services/api';
import ProductsGrid from "@/components/ProductsGrid.vue";
import ArrowLeftIcon from "@/components/icons/ArrowLeftIcon.vue";
import ArrowRightIcon from "@/components/icons/ArrowRightIcon.vue";
import IconButton from "@/components/UI/IconButton.vue";
import AsceticSelect from "@/components/UI/AsceticSelect.vue";
import { useRouter } from 'vue-router';

export default defineComponent({
  components: {
    AsceticSelect,
    IconButton,
    ArrowRightIcon,
    ArrowLeftIcon,
    ProductsGrid,
    Product
  },
  props: {
    category: {
      type: String,
      default: 'all'
    }
  },
  setup(props) {
    const router = useRouter();
    const products = ref([]);
    const page = ref(1);
    const perPage = ref(8);
    const total = ref(0);
    const selectedCategory = ref(null);
    const categories = ref([]);

    const perPageOptions = ref([
      { name: '8', value: '8' },
      { name: '16', value: '16' },
      { name: '20', value: '20' },
    ]);

    const totalPages = computed(() => {
      return Math.ceil(total.value / perPage.value);
    });

    const loadProducts = async () => {
      const category = !selectedCategory.value || selectedCategory.value === 'all' ? null : selectedCategory.value;
      const response = await fetchProducts(page.value, perPage.value, category);
      products.value = response.products;
      total.value = response.total;
      window.scrollTo(0, 0);
    };

    const loadCategories = async () => {
      const response = await fetchCategories();
      categories.value = [{ name: 'All', code: 'all' }, ...response];
    };

    const onPerPageChange = async (newValue) => {
      perPage.value = newValue;
      page.value = 1;
      await loadProducts();
    };

    const nextPage = async () => {
      if (page.value < totalPages.value) {
        page.value++;
        await loadProducts();
      }
    };

    const prevPage = async () => {
      if (page.value > 1) {
        page.value--;
        await loadProducts();
      }
    };

    const filterByCategory = async (category) => {
      page.value = 1;
      selectedCategory.value = category;
      await router.push({ name: 'CategoriesPage', params: { category } });
      await loadProducts();
    };

    onMounted(async () => {
      await loadCategories();
      selectedCategory.value = !props.category || props.category === 'all' ? null : props.category;
      await loadProducts();
    });

    watch(() => props.category, async () => {
      console.log('ProductList watch props.category')
      selectedCategory.value = !props.category || props.category === 'all' ? null : props.category;
      page.value = 1;
      await loadProducts();
    });

    return {
      products,
      page,
      perPage,
      total,
      totalPages,
      nextPage,
      prevPage,
      perPageOptions,
      onPerPageChange,
      categories,
      filterByCategory
    };
  }
});
</script>


<style scoped>
.flex-item + .flex-item {
  margin-top: 2rem;
}

.paginator-btns {
  display: flex;
  gap: .4rem;
}

.product-list {
  margin-top: 3rem;
  margin-bottom: 3rem;
}

.product-list-header {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
}

.filter-btns {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.filter-btns button {
  padding: .6rem 1.6rem;
  cursor: pointer;
  background-color: transparent;
  border: 2px solid rgba(0, 0, 0, 0.3);
  transition: all 0.2s;
}

.filter-btns button:hover {
  border: 2px solid rgba(0, 0, 0, 0.5);
}

.perpage-select {
  width: 8rem;
  justify-self: end;
}

.pagination {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-top: 3rem;
}
</style>
