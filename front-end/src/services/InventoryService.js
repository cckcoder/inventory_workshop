import ApiClient from '@/services/ApiClient.js'

let user = (localStorage.getItem('user')) ? JSON.parse(localStorage.getItem('user')) : null

export default {
  getInventory() {
    return ApiClient.get('/inventory', {
      headers: { Authorization: `Bearer ${user.access_token}` }
    })
  },
  getInventoryById(id) {
    return ApiClient.get(`/inventory/item/${id}`)
  },
  postInventory(inventory) {
    return ApiClient.post('/inventory/item', inventory)
  },
  putInventory(id, inventory) {
    return ApiClient.put(`/inventory/item/${id}`, inventory)
  },
  deleteInventory(id) {
    return ApiClient.delete(`/inventory/item/${id}`)
  }
}
