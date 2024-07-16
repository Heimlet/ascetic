<template>
  <div>
    <div className="news">
      <div className="news-text">
        <h2>Newsletter</h2>
        <form>
          <input type="email" placeholder="your@email.com"/>
          <button type="submit">Subscribe</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
  name: 'Newsletter',
})
</script>

<style scoped>
.news {
  background-color: #191919;
  height: 28rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.news h2 {
  color: white;
  font-size: 3.5rem;
  margin-bottom: 2rem;
}

.news-text {
  text-align: center;
}

.news input {
  font-size: 1.7rem;
  padding: .7rem;
  margin-right: .7rem;
  border: none;
  outline: none;
}

.news button {
  font-size: 1.7rem;
  padding: .7rem;
  border: none;
  cursor: pointer;
}

@media (max-width: 400px) {
  form {
    display: flex;
    flex-direction: column;
    gap: .5rem;
  }

  .news input {
    margin-right: 0;
    text-align: center;
  }
}
</style>

