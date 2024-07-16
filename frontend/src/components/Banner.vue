<template>
  <div class="banner">
    <div class="container">
      <div class="banner-container">
        <div class="text-side">
          <div class="text">
            <h2>{{ title }}</h2>
            <p>{{ text }}</p>
            <router-link to="categories/all">
              <button>Shop now</button>
            </router-link>
          </div>
        </div>
        <div class="img-side">
          <img :src="imageUrl" alt="banner"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {defineComponent, toRefs} from 'vue';

export default defineComponent({
  name: 'Banner',
  props: {
    title: String,
    text: String,
    imageUrl: String,
  },
  setup(props) {
    const {title, text, imageUrl} = toRefs(props);

    return {
      title,
      text,
      imageUrl,
    }
  },
})
</script>

<style scoped>
.banner-container {
  display: flex;
  justify-content: space-between;
  height: 40rem;
  overflow: hidden;
}

.banner-container-reverse {
  display: flex;
  justify-content: space-between;
  height: 40rem;
  overflow: hidden;
  flex-direction: row-reverse;
}

.text-side {
  width: 50%;
  text-align: start;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0 11rem;
  background-color: #E9E9E9;
}

.text-side h2 {
  font-size: 3.2rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.text-side p {
  font-size: 1.8rem;
}

.img-side {
  width: 50%;
  text-align: end;
  background-color: #E9E9E9;
}

.img-side img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.text button {
  background-color: black;
  color: white;
  font-size: 1.7rem;
  font-weight: bold;
  padding: 1rem;
  text-transform: uppercase;
  margin-top: 2rem;
  cursor: pointer;
  border: 2px solid black;
  transition: all 0.15s;
}

.text button:hover {
  background-color: transparent;
  color: black;
}

@media (max-width:750px) {
  .text-side {
    padding: 0 4rem;
  }
}

@media (max-width:600px) {
  .text-side {
    width: 100%;
  }

  .img-side {
    display: none;
  }
}
</style>