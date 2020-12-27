import { createStore } from 'vuex'
import { fetchMetadata, postInsight, postAnswer, postRateAnswer, postRateRelevanceInsight, fetchDownload } from '@/api'

export default createStore({
  state: {
    metadata: [],
    query: '', //query = paperID
    currentIn: '', // Name is not neccessary 
    currentInID: '', // TODO
    currentCategory: '', // TODO
    download: new Blob(),
    currentIn: '', 
    currentAnswer: '', 
    currentCategory: '', 
    answerUpvoteBool: true,
    currentUserInput: '',
    insightVoteBool: null //This boolean is for up- or downvoting insights by the user
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
    setCurrentAnswer (state, payload){
      state.currentAnswer = payload.currentAnswer
    },
    setCategory(state, payload) {
      // TODO when category from backend is available 
      //  state.currentCategory = payload.currentCategory
      },
    setUserInput(state, payload) {
        state.currentUserInput = payload.currentUserInput
    },
    serInsightVoteBool (state, payload) {
          // TODO
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
    // Saves user input for an answer or an insight (yellow and red-status)
    // The difference is that the after commiting the input to the state property, we call slightly different methods "sendAnswer" or "sendInsight"
    fetchUserInput ({commit}, payload) {
      commit('setUserInput', {currentUserInput: payload})
    },
    // Saves user answer (green and yellow-status) that is choosen from the 4 answer posibilites in the Home-Component
    // Not to be confused with the "userInput" that is explaint above 
    // Afterwards "sendRateAnswer" is beeing called with an additional boolean parameter "currentBool"
    fetchUserAnswer ({commit}, payload) {
      commit('setCurrentAnswer', {currentAnswer: payload})
    },
    // Saves current insight name passed from Home-Component
    fetchInName ({commit}, payload) {
      commit('setCurrentInName', {currentIn: payload})
    },

    /*async fetchCurrentCategory ({commit}, payload) {
      await disptach('loadMetadata')
      commit('setCurrentCategory', {currentCategory: payload})
    },
  */


    // TODO: Implement query as paperID when backend is ready
    sendAnswer () {   // DONE
      return postAnswer('50', this.state.currentIn, this.state.currentUserInput)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    // User can rate answer by clicking on it -> green & yellow
    sendRateAnswer () { // DONE
      return postRateAnswer("50", this.state.currentIn, this.state.currentAnswer, this.state.answerUpvoteBool)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
  
    sendInsight () { // TODO when currentyCategory from backend is available 
      return postInsight("50", this.state.userInput, this.state.currentCategory)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },


  // TODO LAST: When everything else works, we might implement this feature
    sendRateRelevanceInsight () {
      return postRateRelevanceInsight("50", this.state.currentIn, this.state.insightVoteBool)
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
  