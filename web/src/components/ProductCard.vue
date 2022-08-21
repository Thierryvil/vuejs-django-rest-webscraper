<script lang="ts">
export default {
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
};
</script>

<template>
  <div class="product-card">
    <img :src="product.image" :alt="product.name" width="300" height="300" />
    <div>
      <p class="product-name">{{ product.name }}</p>
      <p class="product-price">R${{ product.valueTo }}</p>
    </div>
  </div>
</template>

<style scoped>
.product-name {
  font-size: 1rem;
}
.product-card {
  width: 300px;
  height: 500px;
}

.product-price {
  font-weight: bold;
}
</style>
