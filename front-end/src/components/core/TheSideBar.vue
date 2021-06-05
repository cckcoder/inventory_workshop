<template>
    <div class="column is-3 ">
        <aside class="menu">
            <p class="menu-label">
                Generalss
            </p>
            <ul class="menu-list">
                <li
                  v-for="({ name, route }, index) in menus"
                  :key="index"
                >
                  <a @click="handleClickMenu(route)"
                    :class="{ 'is-active' : menuActive == route }">
                    {{ name }}
                  </a>
                </li>
            </ul>
        </aside>
    </div>
</template>

<script>
export default {
  name: 'TheSideBar',
  data() {
    return {
      menus: [
        { name: "Inventory", route: "DashBoard"},
        { name: "Report", route: "Report"},
        { name: "About", route: "About"},
      ]
    }
  },
  methods: {
    handleClickMenu(route) {
      console.log(route)
      this.$router.push({ name: route })
    }
  },
  computed: {
    menuActive() {

      return this.$route.name
    }
  }
}
</script>
