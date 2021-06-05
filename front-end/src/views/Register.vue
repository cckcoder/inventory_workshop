<template>
    <div class="container">
        <div class="columns is-centered">
            <div class="is-full">
              <form @submit.prevent="submitRegister">
                <h1 class="is-size-1 has-text-centered mb-3">
                  Register
                  <i class="fa fa-id-card"></i>
                </h1>
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
                    <button class="button is-link">Register</button>
                  </div>
                  <div class="control">
                    <button class="button is-danger is-light">Cancel</button>
                  </div>
                </div>
                <router-link :to="{ name: 'Login' }">
                    Already have an account? Login.
                  </router-link>
                <p class="has-text-danger	">{{ error }}</p>
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
      password: '',
      error: null
    }
  },
  methods: {
    submitRegister () {
      let formData = new FormData()

      formData.append('username', this.username)
      formData.append('password', this.password)
      this.$store
          .dispatch('register', formData)
          .then(() => {
            this.$router.push({ name: 'DashBoard' })
          })
          .catch(error => {
            console.log(error.response)
            this.error = error.response.data.detail
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
