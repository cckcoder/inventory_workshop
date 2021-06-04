<template>
    <div class="container">
        <div class="columns is-centered">
            <div class="is-full">
              <form @submit.prevent="submitLogin">
                <h1 class="has-text-centered">Login</h1>
                <div class="field">
                  <label class="label">Username</label>
                  <div class="control">
                    <input v-model="username"
                      class="input" type="text" placeholder="Username...">
                  </div>
                </div>
                <div class="field">
                  <label class="label">Password</label>
                  <div class="control">
                    <input v-model="password"
                      class="input" type="password" placeholder="Password...">
                  </div>
                </div>
                <div class="field is-grouped">
                  <div class="control">
                    <button class="button is-link">Login</button>
                  </div>
                  <div class="control">
                    <button class="button is-danger is-light">Cancel</button>
                  </div>
                </div>
              </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitLogin () {
      let formData = new FormData()

      formData.append('username', this.username)
      formData.append('password', this.password)
      this.$store
        .dispatch('login', formData)
        .then(() => {
          this.$router.push({ name: 'DashBoard' })
        })
    }
  }

}
</script>

<style scoped>
.container {
  margin-top: 10%;
}
</style>
