<script setup lang="ts">
import IconSearch from "@/assets/icons/IconSearch.vue";
import { useProductsStore } from "@/store/products";
const { fetchProducts } = useProductsStore();
</script>

<script lang="ts">
export default {
  data() {
    return {
      term: "",
    };
  },
};
</script>

<template>
  <header>
    <nav class="container">
      <p class="logo">LOGO</p>
      <div>
        <input type="search" name="" id="" v-model="term" />
        <button type="submit" @click="fetchProducts(term)">
          <IconSearch />
        </button>
      </div>
    </nav>
  </header>
</template>

<style scoped>
.logo {
  font-weight: bold;
}

div {
  display: flex;
  padding: 2rem;
}

input {
  height: 30px;
  width: 300px;
}

button {
  height: 30px;
}

header {
  background-color: var(--background-color-nav);
  width: 100%;
  height: 60px;
  justify-content: center;
  display: flex;
}

nav {
  display: flex;
  align-items: center;
}
</style>
