<template>
  <div class="product normal">
    <router-link :to="{ name: 'ProductDetails', params: { id: product.id } }">

      <div class="product-header">
        <img :src="product.image" alt="product1"/>
      </div>
      <div class="product-details">
        <p>{{ product.name }}</p>
        <p class="item-price">{{ product.price }} $</p>
      </div>
    </router-link>
  </div>
</template>

<script>
import {defineComponent} from 'vue';

export default defineComponent({
  name: 'Product',
  props: {
    product: Object
  },
});

</script>

<style scoped>
.product {
  outline: 2px solid rgba(0, 0, 0, .205);
  outline-offset: -2px;
  transition: all 0.15s ease-in;
  cursor: pointer;
}

.product > a {
  text-decoration: none;
  color: black;
}

.product:hover {
  outline: 2px solid rgba(0, 0, 0, .7);
}

.product-header img {
  width: 100%;
}

.product-details {
  font-size: 1.7rem;
  padding: 1rem;
}

.item-price {
  font-weight: 600;
  font-size: 2.2rem;
  margin-top: 1.4rem;
}


/* queries */

@media (max-width: 750px) {
  .products-grid {
    grid-template-columns: 1fr 1fr 1fr;
    gap: 2rem;
  }
}

@media (max-width: 600px) {
  .products-grid {
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
