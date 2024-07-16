<template>
  <div>
    <footer>
      <div class="footer-links">
        <a href="#">About</a>
        <a href="#">Store locator</a>
        <a href="#">FAQs</a>
        <a href="#">News</a>
        <a href="#">Careers</a>
        <a href="#">Contact Us</a>
      </div>
      <p class="love">
        Design by
        <a
            target="_blank"
            rel="noreferrer"
            style="color:white;"
        href="https://github.com/Abderraouf-Rahmani"
        >
        Abderraouf
        </a>
      </p>
    </footer>
  </div>
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
  name: 'Footer',
})

</script>

<style scoped>
footer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  height: 17rem;
  background-color: black;

}

.footer-links {
  display: flex;
  gap: 3rem;
  text-align: center;
  flex-wrap: wrap;
  justify-content: center;
}

.footer-links a {
  color: white;
  text-decoration: none;
  font-size: 1.8rem;
}

.footer-links a:hover {
  text-decoration: underline;
}

.love {
  color: white;
  font-size: 1.7rem;
  margin-top: 3rem;
}
</style>