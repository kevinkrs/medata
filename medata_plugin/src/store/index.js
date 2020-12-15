import Vue from 'vue'
import { createStore } from 'vuex'
import { fetchMetadata } from '@/api'

export default createStore({
  state: {
    metadata: []
  },
  mutations: {
    setMetadata (state, payload) {
        state.metadata = payload.metadata
      }
  },
  actions: {
    loadMetadata (context) {
        return fetchMetadata()
          .then((response) => context.commit('setMetadata', {metadata: response.data})) // Mit dieser zeile nochmal beschäftigen!
      }
  },
  modules: {
  },
})
