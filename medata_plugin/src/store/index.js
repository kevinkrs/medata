import Vue from 'vue'
import { createStore } from 'vuex'
import { fetchMetadata, postInsight, postAnswer, postRateAnswer, postRateRelevanceInsight, fetchDownload } from '@/api'

export default createStore({
  state: {
    metadata: [],
    query: '', //query = paperID
    currentIn: '', // Name is not neccessary 
    currentInID: '', // TODO
    currentCategory: '', // TODO
    download: new Blob()
  },
  mutations: {
    // Saving the data from backend to the "metadata array"
    setMetadata (state, payload) {
        state.metadata = payload.metadata
      },
      // This method saves url on acm that user is visiting while using the plugin. The url is submitted to the backend in order to provide the right data
      setQuery (state, payload) {
        // ALWAYS use . operator saving data to the state
        state.query = payload.query
      },
      // 
    setCurrentInName (state, payload){
      state.currentIn = payload.currentIn
    },
    setDownload (state, payload) {
      //may have to use filesaver
      state.download = new Blob([payload.download], { type: 'text/csv;charset=utf-8;' })
    },
    setcurrentInID (state, payload){
      state.currentIn = payload.currentIn
    },
       // sets category from backend to local variable in state
      setCategory(state) {
        state.currentCategory = this.getters.getCategory
      }
  },
  actions: {
    loadQuery({commit}, payload){
      // Important: You have to define what variable the payload should be added to! {query: payload}
      // You can either do this in the $store call or inside the action
      commit('setQuery', {query: payload})
    },
    // Loads methadata and submits acm URL from site user is visiting at the moment to check if data is available
    loadMetadata ({commit}) {
      return fetchMetadata(this.state.query)
        .then((response) => commit('setMetadata', {metadata: response.data})) 
        .catch((error) => {console.error(error)}) 
    },
    loadDownload ({commit}) {
      return fetchDownload(this.state.query)
        .then((response) => commit('setDownload', {download: response.data}))
        .catch((error) => {console.error(error)})
    },
    saveUserInput ({commit}, payload) {
  
      commit('setUserInput', {userInput: payload})
    },
  
    // for user answer input -> yellow and red status 
    sendAnswer (payload) {   
      //await dispatch('fetchUserInput') 
      return postAnswer('50', 'number_outputs', payload)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    // User can rate answer by clicking on it -> green & yellow
    sendRateAnswer () {
      return postRateAnswer("50", this.state.currentInName, this.state.currentAnswer, this.state.currentBool)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
  
    // User input for new insights -> Last div in frontend
    sendInsight () {
      return postInsight("50", this.state.userInput, this.state.currentCategory)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
  // TODO LAST: When everything else works, we might implement this feature
    sendRateRelevanceInsight () {
      return postRateRelevanceInsight("50", this.state.currentInName, this.state.currentBool)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    }
  },
    getters: {
      
    },
  
    modules: {
      
    },
  })
  