import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

const app = createApp(App)
app.config.globalProperties.$pinuser = 'natasha'
app.config.globalProperties.$pinserver = 'http://192.168.50.142:8000'
app.config.globalProperties.$pinpassword = 'ob8y8n9&F*&%Dpf[b09899&^%FD7v[b98hb6705E($976yb[9'
app.use(router)
  .use(store)
  .use(vuetify)
  .mount('#app')
