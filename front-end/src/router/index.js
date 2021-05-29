import { createRouter, createWebHistory } from 'vue-router'
import DashBoard from '@/views/DashBoard'
import CreateInventory from '@/views/CreateInventory'
import EditInventory from '@/views/EditInventory'

const routes = [
  {
    path: '/',
    name: 'DashBoard',
    component: DashBoard
  },
  {
    path: '/create-inventory',
    name: 'CreateInventory',
    component: CreateInventory
  },
  {
    path: '/edit-inventory',
    name: 'EditInventory',
    component: EditInventory,
    props: true
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
