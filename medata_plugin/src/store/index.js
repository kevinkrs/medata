import { createStore } from 'vuex'
import { fetchMetadata, postInsight, postAnswer, postRateAnswer, postRateRelevanceInsight, fetchDownload, postTypoError, postInsightNotRelevant, fetchFurtherInformation, fetchAutocomplete, postBinder } from '@/api'


export default createStore({
/**
 * @Class 
 */
  state: {
    /**
     * Array for saving recieved backend data and access it in every other vue component
     */
    metadata: [],
    /**
     * Current user URL
     */
    query: '', 
    /**
     * Current selected insight name
     */
    currentIn: '', 
    /**
     * Current selected insight ID
     */
    currentInID: '', 
    /**
     * Current CSS categories of visited article 
     */
    currentCategories: [], 
    /**
     * Selected answer by user (yellow-status)
     */
    currentAnswer: '', 
    /**
     * Parameter for backend api request 
     */
    answerUpvoteBool: true,
    /** 
     * Current user input (new insight answer or new insigt)
     */
    currentUserInput: '',
    /**
     * Parameter for backend api request 
     */
    insightVoteBool: true, //This boolean is for up- or downvoting insights by the user, default is true, insight is upvoted @click and only set to false for downvoting via InsightNotRelevantForCategory
    /**
     * Array for saving recieved topic related keywords for autocomplete feature in the _Home.vue_ component
     */
    autocomplete: [],
    /**
     * Array of URL's from binder to request data from backend and trigger direct-download with all the available insight data
     */
    binder: []
  },
  /**
   * @class
   */
  mutations: {
    /**
     * Sets the data recieved from the backend into a state.metadata property in order to be able to access it in other components
     * @param {array} state 
     * @param {array} payload 
     */
    setMetadata (state, payload) {
        state.metadata = payload.metadata
        state.currentCategories = payload.categories
      },
      /**
       * Sets current URL from dl.acm.org that user is visiting when opening the plugin to the state.query property.
       * @param {String} state 
       * @param {String} payload 
       */
    setQuery (state, payload) {
        state.query = payload.query
      },
      /**
       * Sets by user selected (unfolded) insight name to the state.currentIn property.
       * @param {String} state 
       * @param {String} payload 
       */
    setCurrentInName (state, payload){
      state.currentIn = payload.currentIn
    },
    /**
       * Sets by user selected (unfolded) insight ID to the state.currentInID property
       * @param {String} state 
       * @param {String} payload 
       */
    setcurrentInID (state, payload){
      state.currentIn = payload.currentIn
    },
    /**
       * Sets user selected insight answer (yellow-status) to the state.currentAnswer property
       * @param {String} payload 
       */
    setCurrentAnswer (state, payload){
      state.currentAnswer = payload.currentAnswer
    },
    /**
       * Sets user input for submitting either a new insight answer or a completely new insight to the state.currentUserInput property
       * @param {String} state 
       * @param {String} payload 
       */
    setUserInput(state, payload) {
        state.currentUserInput = payload.currentUserInput
    },
    /**
       * Saves the recieved keyword array for the autocomplete feature into a stat.autocomplete property
       * @param {Array} state 
       * @param {Array} payload 
       */
    setAutocomplete(state,payload) {
        state.autocomplete = payload.autocomplete
    },
    /**
       * Saves scraped URL's of users Binder entries to a state.binder property
       * @param {Array} state 
       * @param {Array} payload 
       */
    setBinder(state,payload){
      state.binder = payload.binder
    }
  },
  /**
   * @class
   */
  actions: {
    /**
     * Triggers _mutation_ to save current tab URL if it's valid 
     * @param {String} payload 
     */
    loadQuery({commit}, payload){
      // Important: You have to define what variable the payload should be added to! {query: payload}
      // You can either do this in the $store call or inside the action
      commit('setQuery', {query: payload})
    },
    /**
     * Sends api call to backend in order to recieve available metadata and then passing it to the the fitting _mutation_.
     */
    loadMetadata ({commit}) {
      return fetchMetadata(this.state.query)
        .then((response) => commit('setMetadata', {metadata: response.data.metadata, categories: response.data.categories})) 
        .catch((error) => {console.error(error)}) 
    },
    /**
     * Sends a request to the backend for further information. Backend starts scraper on the forwarded current user URL. 
     */
    loadFurtherInformation () {
      return fetchFurtherInformation(this.state.query)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)}) 
    },
    /**
     * Sends api call to backend to recieve topic related keywords for the autocomplete function and passing it then to the fitting _mutation_.
     *  
     */
    loadAutocomplete({commit}) {
      return fetchAutocomplete(this.state.currentCategories)
        .then((response) => commit('setAutocomplete', {autocomplete: response.data})) 
        .catch((error) => {console.error(error)})
    },



   /**
    * Requests data for the current article or paper and starts a direct download once recieved 
    */
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
    /**
     * Payload is forwarded to _mutation_ to save it into the state.currentUserInput property
     * @param {String} payload 
     */
    fetchUserInput ({commit}, payload) {
      commit('setUserInput', {currentUserInput: payload})
    },
    /**
     * Selected user answer is forwarded to _mutation_ to save it into the state.currentAnswer property 
     * @param {String} payload 
     */
    fetchUserAnswer ({commit}, payload) {
      commit('setCurrentAnswer', {currentAnswer: payload})
    },
    /**
     * Current unfolded insight name is forwarder to _mutation_ to save it into the state.currentInName property
     * @param {String} payload 
     */
    fetchInName ({commit}, payload) {
      commit('setCurrentInName', {currentIn: payload})
    },
   
    /**
     * Scraped Binder URL's are forwarded to _mutation_ to save them into the state.binder property
     * @param {Array} payload 
     */
    fetchBinder({commit}, payload){
      commit('setBinder', {binder: payload})
    },
    

    /**
     * Sends api call to backend for posting a new insight answer (yellow or red-status)
     */
    sendAnswer () {   
      return postAnswer(this.state.query, this.state.currentIn, this.state.currentUserInput)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
   /**
     * Sends api call to backend for rating an insight answer (green or yellow-status)
     */
    sendRateAnswer () { 
      return postRateAnswer(this.state.query, this.state.currentIn, this.state.currentAnswer, this.state.answerUpvoteBool)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    /**
     * Sends api call to backend for posting a new insight
     */
    sendInsight () { 
      return postInsight(this.state.query, this.state.currentUserInput, this.state.currentCategories)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },

    /**
     * Sends api call to backend to upvote insight relevance when unfolding any insight
     */
    sendRateRelevanceInsight () {
      return postRateRelevanceInsight(this.state.query, this.state.currentIn, this.state.insightVoteBool)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    }, 
    /**
     * Sends api call to backend for posting an insight-not-relevant-error (equals double downvote)
     */
    sendInsightNotRelevantError() {
      return postInsightNotRelevant(this.state.currentIn, this.state.currentCategories)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    /**
     * Sends api call to backend for posting a value-error
     */
    sendValueError() {
      return postRateAnswer(this.state.query, this.state.currentIn, this.state.currentAnswer, false)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    /**
     * Sends api call to backend for posting a type-error
     */
    sendTypoError() {
      return postTypoError(this.state.currentIn)
        .then((response) => {console.log(response)})
        .catch((error) => {console.error(error)})
    },
    /**
     * Sends api call to backend forwarding the state.binder array with all Binder URL's and starts direct-downlaod of the csv file after recieving data 
     */
    sendBinder() {
      return postBinder(this.state.binder) 
      .then((response) => {
        var fileURL = window.URL.createObjectURL(new Blob([response.data]))
        var fileLink = document.createElement('a')
        fileLink.href = fileURL
        fileLink.setAttribute('download', 'insights.csv')
        document.body.appendChild(fileLink)
        fileLink.click()
      })
      .catch((error) => {console.error(error)})
    }

  },
    getters: {
    },
  
    modules: {
      
    },
  })
  
