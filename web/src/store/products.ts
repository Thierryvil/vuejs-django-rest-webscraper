import api from "@/services/api";
import { defineStore } from "pinia";

export const useProductsStore = defineStore("products", {
  state: () => ({ products: [], loading: false, term: "" }),
  actions: {
    async fetchProducts(term: string) {
      this.products = [];
      this.term = term.charAt(0).toUpperCase() + term.slice(1);
      this.loading = true;
      try {
        const response = await api.get("/search", { params: { term: term } });
        this.products = response.data;
      } catch (error) {
        // TODO: ADD LOG FILE
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
  },
});
