import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/',
})


export default {
  getInventory() {
    return apiClient.get('/inventory')
  },
  postInventory(inventory) {
    console.log(inventory)
    return apiClient.post('/inventory/item', inventory)
  }
}
