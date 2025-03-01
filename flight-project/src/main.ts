import { createApp } from 'vue'
import { createStore } from 'vuex'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import App from './App.vue'
import router from './router'

import './assets/main.css'

const store = createStore({
  state() {
    return {
      id: '',
      username: '',
      password: '',
      bookings: [],
    }
  },

})
// 从 localStorage 中加载状态
const savedStateString = localStorage.getItem('state')
const savedState = savedStateString ? JSON.parse(savedStateString) : null
if (savedState) {
  store.replaceState(savedState)
}

// 在页面卸载前保存状态到 localStorage 中
window.addEventListener('beforeunload', () => {
  localStorage.setItem('state', JSON.stringify(store.state))
})

const app = createApp(App)
// elementplus-icon
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(router)
  .use(ElementPlus, { size: 'large', zIndex: 3000 })
  .use(store)

app.mount('#app')
