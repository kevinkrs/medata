import { createStore } from 'vuex'
import { fetchMetadata, postInsight, postAnswer, postRateAnswer, postRateRelevanceInsight } from '@/api'

export default createStore({
  state: {
    metadata: [],
    query: '', //query = paperID
    currentIn: '', // Name is not neccessary
    currentAnswer: '', 
    currentCategory: '', // TODO
    currentBool: true,
    currentUserInput: '',
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
    setCurrentAnswer (state, payload){
      state.currentAnswer = payload.currentAnswer
    },
       // sets category from backend to local variable in state
    setCategory(state, payload) {
      //  state.currentCategory = payload.currentCategory
      },
    setUserInput(state, payload) {
        state.currentUserInput = payload.currentUserInput
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
    // Saves user input for an answer or an insight
    fetchUserInput ({commit}, payload) {
      commit('setUserInput', {currentUserInput: payload})
    },
    // Saves user answer (yellow answer fields)
    fetchUserAnswer ({commit}, payload) {
      commit('setCurrentAnswer', {currentAnswer: payload})
    },
    // Saves current insight name
    fetchInName ({commit}, payload) {
      commit('setCurrentInName', {currentIn: payload})
    },

    /*async fetchCurrentCategory ({commit}, payload) {
      await disptach('loadMetadata')
      commit('setCurrentCategory', {currentCategory: payload})
    },
  */


    // for user answer input -> yellow and red status 
    sendAnswer () {   
      //await dispatch('fetchUserInput') 
      return postAnswer('50', this.state.currentIn, this.state.currentUserInput)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    // User can rate answer by clicking on it -> green & yellow
    sendRateAnswer () {
      return postRateAnswer("50", this.state.currentIn, this.state.currentAnswer, this.state.currentBool)
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
      return postRateRelevanceInsight("50", this.state.currentIn, this.state.currentBool)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    }
  },
    getters: {
      getCategory() {
       // return this.state.metadata.category
      }
    },
  
    modules: {
      
    },
  })
  