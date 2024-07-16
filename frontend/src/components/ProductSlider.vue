<template>
  <div class="product-slider">
    <div class="container">
      <div class="title-btns">
        <h3>{{ name }}</h3>
        <div class="btns">
          <IconButton :on-click="slideLeft" >
            <template v-slot:icon>
              <ArrowLeftIcon/>
            </template>
          </IconButton>
          <IconButton :on-click="slideRight" >
            <template v-slot:icon>
              <ArrowRightIcon/>
            </template>
          </IconButton>
        </div>
      </div>
      <div class="row-container" id="slider">
        <Product v-for="product in products" :key="product.id" :product="product" class="row-item"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import Product from "@/components/Product.vue";
import ArrowLeftIcon from "@/components/icons/ArrowLeftIcon.vue";
import ArrowRightIcon from "@/components/icons/ArrowRightIcon.vue";
import IconButton from "@/components/UI/IconButton.vue";

defineProps({
  name: String,
  products: Array,
})

const slideLeft = () => {
  let slider = document.getElementById("slider");
  slider.scrollLeft = slider.scrollLeft - 235;
};

const slideRight = () => {
  let slider = document.getElementById("slider");
  slider.scrollLeft = slider.scrollLeft + 235;
};
</script>

<style>
.row-item {
  outline: 2px solid rgba(0, 0, 0, .205);
  cursor: pointer;
  transition: all 0.15s ease-in;
}

.row-item .product-header img {
  width: 21rem;
}

.row-item .product-details {
  font-size: 1.7rem;
  padding: 1rem;
}

.product-slider h3 {
  font-size: 2.6rem;
  font-weight: 600;
  margin-bottom: 4.2rem !important;
}

.row-container {
  display: flex;
  gap: 2.2rem;
  overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
  scroll-behavior: smooth;
  position: relative;
  padding: 1rem .6rem;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.row-container::-webkit-scrollbar {
  display: none;

  /* Hide scrollbar for IE, Edge and Firefox */
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.title-btns {
  display: flex;
  justify-content: space-between;
}

.btns {
  display: flex;
  gap: .4rem;
}
</style>