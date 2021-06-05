<template>
  <div>
    <NavBar />
    <div class="container mt-6">
      <div class="columns">
        <TheSideBar v-if="loggedIn" />
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/core/NavBar'
import TheSideBar from '@/components/core/TheSideBar'
import { authComputed } from '@/store/helper'

export default {
  components: {
    NavBar,
    TheSideBar
  },
  computed: {
    ...authComputed
  }
}
</script>
