<template>
  <div id="wrapper">
    <nav class="navbar is-info is-light">
      <div class="navbar-brand">
        <router-link :to="{ name: 'DashBoard' }" class="navbar-item">
          <strong>Inventory Workshop</strong>
        </router-link>
      </div>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <div class="navbar-item" v-show="loggedIn">
            <router-link v-if="!loggedIn"
              :to="{ name: 'Login' }"
              class="button">
              Login
            </router-link>
            <button v-else
              @click="logout"
              class="button">
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { authComputed } from '@/store/helper'

export default {
  name: 'NavBar',
  methods: {
    logout() {
      this.$store.dispatch('logout')
    }
  },
  computed: {
    ...authComputed
  }
}
</script>

<style>

</style>
