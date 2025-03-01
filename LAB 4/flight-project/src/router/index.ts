import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import BookingView from '../views/BookingView.vue'
import FlightView from '../views/FlightView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      children: [
        {
          path: '/',
          name: 'booking',
          component: BookingView
        },
        {
          path: '/booking',
          name: 'booking',
          component: BookingView
        },
        {
          path: '/flight',
          name: 'flight',
          component: FlightView
        }
      ]
    },

  ]
})

export default router
