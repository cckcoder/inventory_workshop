import axios from "axios";

const apiClient = axios.create({
  baseURL: 'http://localhost:8001/',
})

export default apiClient
