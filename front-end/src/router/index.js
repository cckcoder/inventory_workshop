import { createRouter, createWebHistory } from 'vue-router'
import DashBoard from '@/views/DashBoard'
import CreateInventory from '@/views/CreateInventory'
import EditInventory from '@/views/EditInventory'
import Login from '@/views/Login'
import Register from '@/views/Register'
import Report from '@/views/Report'

const routes = [
  {
    path: '/dash-board',
    name: 'DashBoard',
    component: DashBoard,
    meta: { requiresAuth: true }
  },
  {
    path: '/report',
    name: 'Report',
    component: Report,
    meta: { requiresAuth: true }
  },
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/create-inventory',
    name: 'CreateInventory',
    component: CreateInventory,
    meta: { requiresAuth: true }
  },
  {
    path: '/edit-inventory',
    name: 'EditInventory',
    component: EditInventory,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem('user')

  if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
    next({ name: 'Login' })
  }

  next()
})

export default router
