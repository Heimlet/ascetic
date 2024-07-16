<template>
  <div class="cart-div" :class="cartOpen ? 'open-cart' : 'closed-cart'">
    <div class="cart-title-btn">
      <h2 class="cart-full-h2">Your Shopping Cart ({{ cartItems.length }})</h2>
      <CloseIcon @click="toggleCart" class="x-mobile"/>
    </div>
    <div class="cart-body">
      <div v-if="cartItems.length < 1" class="empty-cart">
        <p>Your cart is empty</p>
        <button @click="toggleCart">Continue Shopping</button>
      </div>
      <div v-else class="full-cart">
        <div class="full-cart-div">
          <div v-for="item in cartItems" :key="item.id" class="cart-item">
            <div class="cart-img">
              <img :src="item?.details?.image" :alt="item?.details?.name"/>
            </div>
            <div class="cart-middle">
              <div class="cart-name">{{ item?.details?.name }}</div>
              <div class="cart-btns">
                <button @click="decreaseQuantity(item.id)">-</button>
                <p>{{ item.count }}</p>
                <button @click="increaseQuantity(item.id)">+</button>
              </div>
            </div>
            <div class="cart-right">
              <div>{{ item.totalPrice }} $</div>
              <CloseIcon @click="removeItem(item.id)"/>
            </div>
          </div>
        </div>
        <div class="subtotal-div">
          <div class="sub-left">
            <router-link to="/">Checkout</router-link>
          </div>
          <div class="sub-right">
            <div>Subtotal</div>
            <div>{{ subtotal }} $</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, defineComponent } from 'vue';
import { useStore } from 'vuex';
import CloseIcon from "@/components/icons/CloseIcon.vue";

export default defineComponent({
  name: 'Cart',
  components: { CloseIcon },
  props: {
    cartOpen: {
      type: Boolean,
      required: true
    },
    toggleCart: {
      type: Function,
      required: true
    }
  },
  setup() {
    const store = useStore();
    const cartItems = computed(() => store.getters["cart/cartItems"]);
    const subtotal = computed(() => store.getters["cart/subtotal"]);

    const removeItem = (itemId) => {
      store.dispatch('cart/removeItemFromCart', itemId);
    };

    const increaseQuantity = (itemId) => {
      store.dispatch('cart/increaseQuantity', itemId);
    };

    const decreaseQuantity = (itemId) => {
      store.dispatch('cart/decreaseQuantity', itemId);
    };

    return {
      cartItems,
      removeItem,
      increaseQuantity,
      decreaseQuantity,
      subtotal
    };
  }
});
</script>


<style scoped>
.cart-div {
  display: flex;
  flex-direction: column;
  position: fixed;
  z-index: 999;
  top: 0;
  right: 0;
  padding: 3rem 2.5rem 1.5rem 2.5rem;
  background-color: white;
  height: 100vh;
  width: 50rem;
  transition: all 0.4s ease;
}

.cart-title-btn {
  font-size: 1.7rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cart-full-h2 {
  font-size: 2.1rem !important;
}

.cart-title-btn i {
  font-size: 2.5rem;
  cursor: pointer;
}

.cart-body {
  height: 100vh;
  padding: 0.5rem;
}

.empty-cart {
  display: flex;
  flex-direction: column;
  text-align: center;
  width: 16rem;
  margin: 15rem auto;
}

.empty-cart p {
  font-size: 2rem;
  font-weight: 600;
  margin-top: 1rem;
}

.empty-cart button {
  width: 100%;
  height: 4.4rem;
  font-size: 1.7rem;
  margin-top: 3rem;
  cursor: pointer;
}

.closed-cart {
  right: -100%;
}

.open-cart {
  right: 0;
}

.full-cart {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.full-cart-div {
  overflow-y: scroll;
  padding: 5px;
  height: 70%;
  margin-top: 2rem;
  margin-right: -.5rem;
}

.cart-item {
  width: 100%;
  height: 15rem;
  display: grid;
  grid-template-columns: 30fr 50fr 20fr;
  border: 1px solid #717171;
  border-radius: 3px;
  background-color: #f2f2f2;
}

.cart-img {
  width: 100%;
  height: 100%;
  background-color: white;
}

.cart-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 3px;
}

.cart-middle {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 1.5rem;
}

.cart-btns {
  display: flex;
}

.cart-btns button {
  font-size: 2rem;
  width: 3rem;
  height: 3rem;
  background-color: black;
  color: white;
  cursor: pointer;
}

.cart-btns p {
  font-size: 2rem;
  outline: 2px solid black;
  outline-offset: -2px;
  width: 3rem;
  text-align: center;
  padding-top: 3.5px;
}

.cart-name {
  font-size: 2.4rem;
}

.cart-right {
  display: flex;
  flex-direction: column;
  text-align: right;
  justify-content: space-between;
  padding: 1.5rem;
  font-size: 2.4rem;
  font-weight: 600;
}

.cart-right i {
  cursor: pointer;
}

/* subtotal */
.subtotal-div {
  display: flex;
  width: 100%;
  height: 12rem;
  border-top: 2px dashed black;
  margin-top: 1.5rem;
  padding: 1rem 0;
  justify-content: space-between;
}

.sub-right {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  font-size: 2.5rem;
  font-weight: 600;
}

.sub-left a {
  font-size: 2rem;
  color: black;
  border: 2px solid black;
  text-decoration: none;
  background-color: transparent;
  padding: 1rem 3.5rem;
  transition: all 0.2s;
}

.sub-left a:hover {
  background-color: #000000;
  color: white;
}

.sub-left {
  padding-top: 4rem;
}

@media (max-width: 420px) {
  .cart-item {
    grid-template-columns: 1fr;
    height: 100%;
    width: 90%;
  }

  .full-cart {
    align-items: center;
  }

  .cart-middle {
    align-items: center;
    gap: 2rem;
  }

  .cart-right {
    text-align: center;
    flex-direction: row;
  }

  .subtotal-div {
    flex-direction: column;
    align-items: center;
  }
}
</style>
