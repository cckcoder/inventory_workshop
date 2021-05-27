import { createStore } from 'vuex'
import InventoryService from '@/services/InventoryService.js'

export default createStore({
  state: {
    inventory: []
  },
  mutations: {
    SET_INVENTORY(state, inventory) {
      state.inventory = inventory
    },
    ADD_INVENTORY(state, inventory) {
      console.log(state + '\n')
      console.log(inventory)
      //state.inventory.push(inventory)
    }
  },
  actions: {
    fetchInventory({ commit }) {
      InventoryService.getInventory()
        .then(response => {
          console.log(response.data)
          commit('SET_INVENTORY', response.data)
        })
    },
    createInventory({ commit }, inventory) {
      InventoryService.postInventory(inventory)
      commit('ADD_INVENTORY', inventory)
    }

  },
  modules: {
  }
})
