<template>
  <h1>Hello Inventor Workshop</h1>
  <p>test</p>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch('fetchInventory')
  },



}
</script>

<style>

</style>
