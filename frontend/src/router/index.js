import { createRouter, createWebHashHistory } from 'vue-router'
import InfluencerView from '../views/InfluencerView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: InfluencerView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/register',
    name:'register',
    component: ()=>import('../views/Register.vue')
  },
  {
    path:'/login',
    name:'login',
    component: ()=>import('../views/Login.vue')
  },
  {
    path:'/SponsorView',
    name:'sponsor',
    component:()=>import('../views/SponsorView.vue')
  }
]


const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
