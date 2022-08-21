import axios from "axios";
const apiBaseUrl = import.meta.env.VITE_APP_API_BASE_URL;

const api = axios.create({
  baseURL: apiBaseUrl,
});

export default api;
