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
          <div class="navbar-item">
            <div class="buttons">
            <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
            </template>
            <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
            </template>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
