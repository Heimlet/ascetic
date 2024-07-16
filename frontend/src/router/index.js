import { createRouter, createWebHistory } from 'vue-router';
import CategoriesPage from '../views/CategoriesPage.vue';
import HomePage from "@/views/HomePage.vue";
import ProductPage from "@/views/ProductPage.vue";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/categories/product/:id',
    name: 'ProductDetails',
    component: ProductPage,
    props: true
  },
  {
    path: '/categories/:category?',
    name: 'CategoriesPage',
    component: CategoriesPage,
    props: true
  },
  {
    path: '/:catchAll(.*)',
    redirect: '/'
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
