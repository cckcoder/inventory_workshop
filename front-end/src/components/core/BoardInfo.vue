<template>
  <div class="column is-9">
      <section class="hero is-info welcome is-small">
          <div class="hero-body">
              <div class="container">
                  <h1 class="title">
                      Hello, {{ showUser }}
                  </h1>
                  <h2 class="subtitle">
                      I hope you are having a great day!
                  </h2>
              </div>
          </div>
      </section>
      <section class="info-tiles mt-4">
          <div class="tile is-ancestor has-text-centered">
              <div class="tile is-parent">
                  <article class="tile is-child box">
                      <p class="title">439k</p>
                      <p class="subtitle">Users</p>
                  </article>
              </div>
              <div class="tile is-parent">
                  <article class="tile is-child box">
                      <p class="title">59k</p>
                      <p class="subtitle">Products</p>
                  </article>
              </div>
              <div class="tile is-parent">
                  <article class="tile is-child box">
                      <p class="title">3.4k</p>
                      <p class="subtitle">Open Orders</p>
                  </article>
              </div>
              <div class="tile is-parent">
                  <article class="tile is-child box">
                      <p class="title">19</p>
                      <p class="subtitle">Exceptions</p>
                  </article>
              </div>
          </div>
      </section>

      <div class="columns mt-4">
          <div class="column is-3 is-offset-9">
              <button @click="$router.push({ name: 'CreateInventory' })"
                  class="button is-primary is-fullwidth">
                  <i class="fa fa-plus-circle mr-1" aria-hidden="true"></i>
                  Create inventory
              </button>
          </div>
      </div>
      <div class="columns">
          <div class="column is-full">
            <table class="table is-striped is-fullwidth">
            <thead class="has-text-centered">
                <tr>
                    <th v-for="column in columnsHeader" :key="column">{{ column }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in inventory" :key="item.id" class="has-text-centered">
                    <td>{{ item.id }}</td>
                    <td>
                        <ImageBase :image_name="item.image_name" />
                    </td>
                    <td>{{ item.name }}</td>
                    <td>{{ item.price }}</td>
                    <td>{{ item.stock }}</td>
                    <td class="has-text-centered">
                        <div class="buttons is-inline-block">
                            <button class="button is-warning mr-3">
                                <router-link :to="{ name: 'EditInventory', params: { id: item.id} }">
                                    <i class="fa fa-pencil-square-o mr-1"></i>
                                    Edit
                                </router-link>
                            </button>
                            <button @click="deleteItem(item.id)"
                                class="button is-danger">
                                <i class="fa fa-times mr-1"></i>
                                Delete
                            </button>
                        </div>
                    </td>
                </tr>
            </tbody>
            </table>
          </div>
      </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { userComputed } from '@/store/helper'
import ImageBase from '@/components/core/ImageBase'

export default {
  data() {
      return {
          columnsHeader: ['ID', 'image', 'name', 'price', 'stock', 'Activity']
      }
  },
  components: {
      ImageBase
  },
  created() {
      this.$store .dispatch('fetchInventory')
  },
  methods: {
    deleteItem(id) {
      this.$store.dispatch('deleteInventory', id)
    }
  },
  computed: {
    ...userComputed,
    ...mapState(['inventory'])
  }

}
</script>

<style scoped>
a {
    color: #ffffff;
    text-decoration: none;
}

a:hover {
    cursor: pointer;
}
</style>
