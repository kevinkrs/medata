import Vue from 'vue'
import App from './App.vue'
import webpack from '../node-modules/webpack-extension-reloader'

Vue
/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App)
})
