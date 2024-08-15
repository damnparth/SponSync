import { createApp } from 'vue'
import PrimeVue from "primevue/config";
import Password from 'primevue/password';
import App from './App.vue'
import router from './router'
import store from './store'

   
import 'primeicons/primeicons.css'; 



createApp(App).use(store).use(router).mount('#app')
App.use(PrimeVue, { inputStyle: 'filled' });





