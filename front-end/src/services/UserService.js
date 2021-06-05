import ApiClient from '@/services/ApiClient.js'

export default {
  getLogin(credentials) {
    return ApiClient.post('/user/login', credentials)
  },
  getRegister(credentials) {
    return ApiClient.post('/user/register', credentials)
  }
}
