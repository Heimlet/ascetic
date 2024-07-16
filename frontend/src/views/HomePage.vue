<template>
  <div class="container">
    <div class="flex-item">
      <Header/>
    </div>
    <div class="flex-item">
      <ProductsGrid :products="proudProducts" grid-name="Products we are proud of"/>
    </div>
    <div class="flex-item">
      <Banner
          title="Creative harmonious living"
          text=" RAOUF Products are all made to standard sizes so that you can mix and match them freely."
          :image-url="banner1"
      />
    </div>
    <div class="flex-item">
      <ProductSlider name="Trending Now" :products="trendingProducts"/>
    </div>
  </div>
</template>

<script setup>
import Banner from "@/components/Banner.vue";
import Header from "@/components/Header.vue";
import ProductsGrid from "@/components/ProductsGrid.vue";
import {onMounted, ref} from "vue";
import {fetchProducts} from "@/services/api.js";
import ProductSlider from "@/components/ProductSlider.vue";
import banner1 from "@/assets/images/banner/banner1.jpg";

const proudProducts = ref([]);
const trendingProducts = ref([]);
const resp = ref(null);
const counter = ref(0);

onMounted(async () => {
  fetchProducts(null, null, null, null, true)
      .then((response) => proudProducts.value = response.products)

  fetchProducts(null, null, null, true, null)
      .then((response) => trendingProducts.value = response.products)
})


</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-bottom: 5rem;
}

.flex-item + .flex-item {
  margin-top: 10rem;
}
</style>