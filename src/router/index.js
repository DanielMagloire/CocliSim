import Vue from 'vue'
import VueRouter from 'vue-router'
import About from '../views/About.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'About',
    component: About
  },
  {
    path: '/confort-climatique',
    name: 'confort climatique',
    component: () => import('../views/Confort.vue')
  },
  {
    path: '/inconfort-thermique',
    name: 'inconfort thermique',
    component: () => import('../views/Inconfort.vue')
  },
  {
    path: '/courant-air',
    name: 'courant d\'air',
    component: () => import('../views/courantAir.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
