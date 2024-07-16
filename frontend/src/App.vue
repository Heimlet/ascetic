<template>
  <Navbar/>
  <div class="main">
    <div class="content">
      <router-view/>
    </div>
    <div class="footer">
      <Newsletter/>
      <Footer/>
    </div>
  </div>
</template>

<script>
import {defineComponent} from 'vue';
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
import Newsletter from "@/components/Newsletter.vue";

export default defineComponent({
  name: 'App',
  components: {Newsletter, Navbar, Footer}
});
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100vh;
}

.content {
  padding-top: 12rem;
}

.footer {
  align-self: flex-end;
  width: 100%;
}

</style>
