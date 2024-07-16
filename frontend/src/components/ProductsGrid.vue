<template>
  <div>
    <div class="p-grid-container">
      <h2 v-if="gridName" class="container p-grid-h2">{{ gridName }}</h2>

      <div class="container">
        <div class="products-grid">
          <Product v-for="item in products" :key="item.id" :product="item"/>
        </div>
      </div>

    </div>
  </div>

</template>

<script setup>
import Product from "@/components/Product.vue";

defineProps({
  products: Array,
  gridName: String,
})
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}

.p-grid-h2 {
  font-size: 2.6rem;
  font-weight: 600;
  margin-bottom: 4.2rem;
}

.products-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 2rem;
}

/* queries */

@media (max-width: 750px) {
  .products-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 2rem;
  }
}

@media (max-width: 600px) {
  .products-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
}

@media (max-width: 430px) {
  .products-grid {
    grid-template-columns: 1fr;
  }
}
</style>