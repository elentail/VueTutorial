import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueCodeHighlight from "vue-code-highlight";

//전역 설정
Vue.use(BootstrapVue)
Vue.use(VueCodeHighlight);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
