import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import Highcharts from 'highcharts'

import More from 'highcharts/highcharts-more'

More(Highcharts)
Vue.config.productionTip = false


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
