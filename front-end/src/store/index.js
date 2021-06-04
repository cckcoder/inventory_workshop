import { createStore } from 'vuex'
import InventoryService from '@/services/InventoryService.js'
import UserService from '@/services/UserService.js'

export default createStore({
  state: {
    inventory: [],
    itemInventory: {},
    user: null
  },
  mutations: {
    SET_INVENTORY(state, inventory) {
      state.inventory = inventory
    },
    SET_ITEM_INVENTORY(state, itemInventory) {
      state.itemInventory = itemInventory
    },
    ADD_INVENTORY(state, inventory) {
      console.log(state + '\n')
      console.log(inventory)
      //state.inventory.push(inventory)
    },
    UPDATE_ITEM_INVENTORY(state, itemInventory) {
      state.itemInventory = itemInventory
    },
    DEL_INVENTORY(state, id) {
      state.inventory = state.inventory.filter(item => item.id !== id)
    },
    SET_USER_DATA(state, userData) {
      state.user = userData
      localStorage.setItem('user', JSON.stringify(userData))
    }
  },
  actions: {
    fetchInventory({ commit }) {
      InventoryService.getInventory()
        .then(response => {
          commit('SET_INVENTORY', response.data)
        })
    },
    fetchInventoryById ({ commit }, id) {
      InventoryService.getInventoryById(id)
        .then(resp => {
          commit('SET_ITEM_INVENTORY', resp.data)
        })

    },
    createInventory({ commit }, inventory) {
      InventoryService.postInventory(inventory)
          .then(resp => {
            commit('ADD_INVENTORY', resp.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
    updateInventory({ commit }, { id, formData }) {
      InventoryService.putInventory(id, formData)
          .then(resp => {
            commit('UPDATE_ITEM_INVENTORY', resp.data)
          })
    },
    deleteInventory({ commit }, id) {
      InventoryService.deleteInventory(id)
        .then(resp => {
            if (resp.status === 200) {
              commit('DEL_INVENTORY', id)
            } else {
              console.log('Something wrong.')
            }
        })
        .catch(error => {
          console.log(error)
        })
    },
    login({ commit }, credentials) {
      UserService.getLogin(credentials)
        .then(({ data }) => {
          commit('SET_USER_DATA', data)
      })
    }

  },
  getters: {
    loggedIn(state) {
      return !!state.user
    }
  },
  modules: {
  }
})
