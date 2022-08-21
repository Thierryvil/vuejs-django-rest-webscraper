<script setup lang="ts">
import { storeToRefs } from "pinia";
import "./assets/global.css";
import HeaderComponent from "./components/HeaderComponent.vue";
import ProductCard from "./components/ProductCard.vue";
import LoaderComponent from "./components/LoaderComponent.vue";
import { useProductsStore } from "./store/products";
const { products, term, loading } = storeToRefs(useProductsStore());
</script>

<template>
  <HeaderComponent />

  <LoaderComponent :loading="loading" />

  <div class="products">
    <p class="product-term" v-if="products.length > 0">
      Pesquisa para: {{ term }}
    </p>
    <div class="products-list">
      <div v-for="(product, index) in products" :key="index">
        <ProductCard :product="product" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.products-list {
  display: grid;
  gap: 1px;
  grid-template-columns: repeat(3, 1fr);
  margin-left: 185px;
}

.product-term {
  font-size: 1.2rem;
  color: #cdcdcd;
  margin: 2rem;
  margin-left: 185px;
  font-family: "Urban Grotesk";
}
</style>
