import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/',
})


export default {
  getInventory() {
    return apiClient.get('/inventory')
  },
  getInventoryById(id) {
    return apiClient.get(`/inventory/item/${id}`)
  },
  postInventory(inventory) {
    return apiClient.post('/inventory/item', inventory)
  },
  putInventory(id, inventory) {
    return apiClient.put(`/inventory/item/${id}`, inventory)
  },
  deleteInventory(id) {
    return apiClient.delete(`/inventory/item/${id}`)
  }
}
