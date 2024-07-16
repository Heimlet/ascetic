<template>
  <div>
    <!-- Mobile Navigation -->
    <div :class="['mobile-nav-full', mobileNav ? 'open-flex' : 'closed-flex']">
      <i @click="toggleMobileNav" class="x-mobile">
        <CloseIcon/>
      </i>
      <div class="mobile-links">
        <router-link @click.native="toggleMobileNav" to="/categories/all">Categories</router-link>
        <router-link @click.native="toggleMobileNav" :to="{ name: 'CategoriesPage', params: { 'category' : 'lamp' }}">Lamps</router-link>
        <router-link @click.native="toggleMobileNav" to="/categories/product/19">Product Page</router-link>
      </div>
    </div>

    <!-- Overlay -->
    <div @click="toggleCart" :class="['page-overlay', cartOpen ? 'open-flex' : 'closed-flex']"></div>

    <!-- Cart -->
    <Cart :cartOpen="cartOpen" :toggleCart="toggleCart"/>

    <!-- Navbar -->
    <nav class="navbar">
      <div class="container">
        <div :class="['nav-container', sticky ? 'cont-sticky' : '']">
          <router-link to="/">
            <img @click="scrollToTop" :src="logoImg" alt="logo" class="logo-img"/>
          </router-link>
          <div class="nav-links">
            <router-link @click.native="scrollToTop" to="/categories/all">Categories</router-link>
            <router-link @click.native="scrollToTop" to="/categories/lamp">Lamps</router-link>
            <i
                :data-array-length="cartItems.length"
                @click="toggleCart"
                class="hamburger-cart"
            >
              <CartIcon :count="cartItems.length"/>
            </i>
          </div>
          <div class="hamburger-menu">
            <i
                :data-array-length="cartItems.length"
                @click="toggleCart"
                class="hamburger-cart"
            >
              <CartIcon :count="cartItems.length" size="large"/>
            </i>
            <i @click="toggleMobileNav" class="hamburger-hamb">
              <MenuIcon/>
            </i>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import {onMounted, onUnmounted, ref} from 'vue';
import {useStore} from 'vuex';
import LogoImg2 from '@/assets/images/newlogo2.png';
import Cart from '@/components/Cart.vue';
import CartIcon from "@/components/icons/CartIcon.vue";
import MenuIcon from "@/components/icons/MenuIcon.vue";
import CloseIcon from "@/components/icons/CloseIcon.vue";

export default {
  name: 'Navbar',
  components: {
    CloseIcon,
    MenuIcon,
    CartIcon,
    Cart,
  },
  setup() {
    const sticky = ref(false);
    const mobileNav = ref(false);
    const cartOpen = ref(false);
    const logoImg = LogoImg2;

    const store = useStore();
    const cartItems = store.state.cart.cartItems;

    const handleScroll = () => {
      sticky.value = window.scrollY > 10;
    };

    const toggleCart = () => {
      cartOpen.value = !cartOpen.value;
    };

    const toggleMobileNav = () => {
      mobileNav.value = !mobileNav.value;
    };

    const scrollToTop = () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
    });

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll);
    });

    return {
      sticky,
      mobileNav,
      cartOpen,
      logoImg,
      cartItems,
      handleScroll,
      toggleCart,
      toggleMobileNav,
      scrollToTop
    };
  }
};
</script>

<style scoped>
.navbar {
  -webkit-box-shadow: 0px 4px 5px -5px rgba(0, 0, 0, 0.23);
  -moz-box-shadow: 0px 4px 5px -5px rgba(0, 0, 0, 0.23);
  box-shadow: 0px 4px 5px -5px rgba(0, 0, 0, 0.23);
  background-color: white;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 100;
  padding: 0 1rem;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 12rem;
  transition: height 0.1s linear;
}

.nav-container.cont-sticky {
  height: 8rem !important;
}

.logo-img {
  width: 8.5rem;
  height: auto;
  cursor: pointer;
}

.nav-links {
  font-size: 1.8rem;
  text-transform: uppercase;
  display: flex;
  gap: 2.5rem;
}

.nav-links a {
  color: #000000;
  text-decoration: none;
}

.nav-links a:hover {
  text-decoration: underline;
}

.nav-links i {
  cursor: pointer;
  display: flex;
  align-items: center;
}

.hamburger-menu {
  display: none;
  gap: 3rem;
}

.hamburger-hamb,
.hamburger-cart {
  font-size: 2.3rem;
  display: none;
  cursor: pointer;
}

.mobile-nav-full {
  background-color: #f3f3f3;
  z-index: 200;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.open-flex {
  display: flex !important;
}

.closed-flex {
  display: none !important;
}

.mobile-nav-full i {
  font-size: 2.3rem;
  position: absolute;
  right: 25px;
  top: 49px;
  cursor: pointer;
}

.mobile-links {
  font-size: 3rem;
  text-transform: uppercase;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  justify-content: center;
  align-items: center;
  top: 44%;
  left: 50%;
  position: absolute;
  transform: translate(-50%, -50%);
}

.mobile-links a {
  color: black;
  text-decoration: none;
}

.mobile-links a:hover {
  text-decoration: underline;
}

/* cart icon */
.cart-icon {
  position: relative;
  display: flex;
  align-items: center;
}

.cart-icon::after {
  content: '';
  top: -18px;
  position: absolute;
  left: 12px;
  font-size: 11px;
  background-color: #b6002c;
  color: white;
  padding: 5px;
  border-radius: 50%;
  width: 10px;
  height: 10px;
  text-align: center;
  display: none;
}

.cart-icon.with-items::after {
  content: attr(data-array-length);
  top: -18px;
  position: absolute;
  left: 12px;
  font-size: 13px;
  background-color: #b6002c;
  color: white;
  padding: 5px;
  border-radius: 50%;
  width: 10px;
  height: 10px;
  text-align: center;
  display: flex;
  align-items: center;
  z-index: 999;
}

.page-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #00000075;
  z-index: 888;
  transition: all 0.3s ease-in;
}

/* responsive */
@media (max-width: 600px) {
  .nav-links {
    display: none;
  }

  .hamburger-menu {
    display: flex;
  }

  .hamburger-cart,
  .hamburger-hamb {
    display: flex;
  }

  .cart-div {
    width: 100%;
  }
}
</style>
