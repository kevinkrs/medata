import { createStore } from 'vuex'
import { fetchMetadata, postInsight, postAnswer, postRateAnswer, postRateRelevanceInsight, fetchDownload, postTypoError, postInsightNotRelevant, fetchFurtherInformation, fetchAutocomplete, postBinder } from '@/api'


export default createStore({
  state: {
    metadata: [],
    query: '', //query = paperID
    currentIn: '', 
    currentInID: '', 
    currentCategories: [], 
    currentIn: '', 
    currentAnswer: '', 
    answerUpvoteBool: true,
    currentUserInput: '',
    selectedError: '', // User can report an error and select on of three possibilites
    insightVoteBool: true, //This boolean is for up- or downvoting insights by the user, default is true, insight is upvoted @click and only set to false for downvoting via InsightNotRelevantForCategory
    autocomplete: [],
    binder: []
  },
  mutations: {
    // Saving the data from backend to the "metadata array"
    setMetadata (state, payload) {
        state.metadata = payload.metadata
        state.currentCategories = payload.categories
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
    setcurrentInID (state, payload){
      state.currentIn = payload.currentIn
    },
    setCurrentAnswer (state, payload){
      state.currentAnswer = payload.currentAnswer
    },
    setUserInput(state, payload) {
        state.currentUserInput = payload.currentUserInput
    },
    setSelectedError(state,payload) {
        state.selectedError = payload
    },
    setAutocomplete(state,payload) {
        state.autocomplete = payload.autocomplete
    },
    setBinder(state,payload){
      state.binder = payload.binder
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
        .then((response) => commit('setMetadata', {metadata: response.data.metadata, categories: response.data.categories})) 
        .catch((error) => {console.error(error)}) 
    },
    loadFurtherInformation () {
      return fetchFurtherInformation(this.state.query)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)}) 
    },
    loadAutocomplete({commit}) {
      return fetchAutocomplete(this.state.currentCategories)
        .then((response) => commit('setAutocomplete', {autocomplete: response.data})) 
        .catch((error) => {console.error(error)})
    },



    // Triggers function to get a csv file with the current insights and send it to the FE. User gets possibility to download data
    loadDownload () {
      return fetchDownload(this.state.query)
        .then((response) => {
          var fileURL = window.URL.createObjectURL(new Blob([response.data]))
          var fileLink = document.createElement('a')
          fileLink.href = fileURL
          fileLink.setAttribute('download', 'insights.csv')
          document.body.appendChild(fileLink)
          fileLink.click()
        })
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
    // DEPRICATED -> Error name not relevant, click on error button dispatches the right call to backend

    fetchBinder({commit}, payload){
      commit('setBinder', {binder: payload})
    },
    


    sendAnswer () {   // DONE
      return postAnswer(this.state.query, this.state.currentIn, this.state.currentUserInput)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    // User can rate answer by clicking on it -> green & yellow
    sendRateAnswer () { // DONE
      return postRateAnswer(this.state.query, this.state.currentIn, this.state.currentAnswer, this.state.answerUpvoteBool)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
  
    sendInsight () { // NOT TESTED YET
      return postInsight(this.state.query, this.state.currentUserInput, this.state.currentCategories)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },

    sendRateRelevanceInsight () {
      return postRateRelevanceInsight(this.state.query, this.state.currentIn, this.state.insightVoteBool)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    }, 
    sendInsightNotRelevantError() {
      return postInsightNotRelevant(this.state.currentIn, this.state.currentCategories)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    sendValueError() {
      return postRateAnswer(this.state.query, this.state.currentIn, this.state.currentAnswer, false)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    sendTypoError() {
      return postTypoError(this.state.currentIn)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    //TODO
    sendBinder() {
      return postBinder(this.state.binder) 
      .then((response) => {console.log(response)})
      .cach((error) => {console.log(error)})
    }

  },
    getters: {
    },
  
    modules: {
      
    },
  })
  
