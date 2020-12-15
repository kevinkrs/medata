import Vue from 'vue'
import { createStore } from 'vuex'
import { fetchMetadata, postInsight, postAnswer, postRateAnswer, postRateRelevanceInsight } from '@/api'

export default createStore({
  state: {
    metadata: [],
    query: ''
  },
  mutations: {
    setMetadata (state, payload) {
        state.metadata = payload.metadata
      },
      setQuery (state, payload) {
        // ALWAYS use . operator saving data to the state
        state.query = payload.query
      }
  },
  actions: {
  loadQuery(context, payload){
    // Important: You have to define what variable the payload should be added to! {query: payload}
    // You can either do this in the $store call or inside the action
    context.commit('setQuery', {query: payload})
  },
  loadMetadata (context) {
      return fetchMetadata()
        .then((response) => context.commit('setMetadata', {metadata: response.data})) 
        .catch((error) => {console.error(error)}) 
  },
  sendInsight (inPaperId, inInsight, inCategories) {
    //contex?
    let a = inPaperId
    let b = inInsight
    let c = inCategories
    //e.g. hardcoded 4 now
    a = 102
    b = "postman_insight3"
    c = ["cat5", "cat6"]
    return postInsight(a, b, c)
      .then((response) => {console.log(response)})
      .catch((error) => {console.error(error)})
  },
  sendAnswer (inPaperId, inInsight, inAnswer) {
    //contex?
    let a = inPaperId
    let b = inInsight
    let c = inAnswer
    //e.g. hardcoded 4 now
    a = 56
    b = "number_inputs"
    c = "POSTMAN_from_vue"
    return postAnswer(a, b, c)
      .then((response) => {console.log(response)})
      .catch((error) => {console.error(error)})
  },
  sendRateAnswer (inPaperId, inInsight, inAnswer, inUpvote) {
    //contex?
    let a = inPaperId
    let b = inInsight
    let c = inAnswer
    let d = inUpvote
    //e.g. hardcoded 4 now
    a = 56
    b = "number_inputs"
    c = "answer1"
    d = True
    return postRateAnswer(a, b, c, d)
      .then((response) => {console.log(response)})
      .catch((error) => {console.error(error)})
  },
  sendRateRelevanceInsight (inPaperId, inInsight, inUpvote) {
    //contex?
    let a = inPaperId
    let b = inInsight
    let c = inUpvote
    //e.g. hardcoded 4 now
    a = 56
    b = "number_inputs"
    c = True
    return postRateRelevanceInsight(a, b, c)
      .then((response) => {console.log(response)})
      .catch((error) => {console.error(error)})
  },
},

  modules: {
  },
})
