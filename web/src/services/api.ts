import axios from "axios";

const api = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL ?? "http://localhost:8000/api",
});

export default api;
