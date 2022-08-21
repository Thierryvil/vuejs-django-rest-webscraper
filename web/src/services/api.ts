import axios from "axios";
const apiBaseUrl = import.meta.env.VUE_APP_API_BASE_URL;

const api = axios.create({
  baseURL: apiBaseUrl ?? "http://localhost:8000/api",
});

export default api;
