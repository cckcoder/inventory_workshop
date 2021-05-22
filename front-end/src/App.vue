<template>
  <div>
    <CreateInvent />
  </div>
</template>

<script>
import CreateInvent from '@/components/CreateInventory'
export default {
  name: "App",
  components: {
    CreateInvent
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
