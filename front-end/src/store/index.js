import { createStore } from 'vuex'
import InventoryService from '@/services/InventoryService.js'

export default createStore({
  state: {
    inventory: []
  },
  mutations: {
    SET_INVENTORY(state, event) {
      state.inventory = event
    }
  },
  actions: {
    fetchInventory({ commit }) {
      InventoryService.getInventory()
        .then(response => {
          console.log(response.data)
          commit('SET_INVENTORY', response.data)
        })
    }

  },
  modules: {
  }
})
