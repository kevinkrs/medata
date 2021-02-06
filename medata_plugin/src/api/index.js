import axios from 'axios'



axios.defaults.baseURL = 'http://193.196.38.100:5000'

axios.defaults.headers.common ['Content-Type']= 'application/json'

/**
 * Axios post request for sending current user URL to backend and recieves insight data for forwarded paper/ article URL.
 * @param {String} query 
 */
export function fetchMetadata (query) {
  return axios.post(`${'get_specific'}`, {url: query})
}

/**
 * Axios post request for sending current user URL to backend and starting backend scraper to get further information.
 * @param {String} query 
 */
export function fetchFurtherInformation (query) {
  return axios.post(`${'get_further_information'}`, {url: query})
}

/**
 * Axios post request that sends an upvote (bolean) to highten relevance for certain insight selected by the user.
 * @param {String} inPaperId 
 * @param {String} inInsight 
 * @param {Boolean} inUpvote 
 */
export function postRateRelevanceInsight (inPaperId, inInsight, inUpvote) {
  return axios.post(`${'rate_relevance_insight'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    upvote: inUpvote
  })
}

/**
 * Axios post request that sends new answer for an insight added by the user to the backend.
 * @param {String} inPaperId 
 * @param {String} inInsight 
 * @param {String} inAnswer 
 */
export function postAnswer (inPaperId, inInsight, inAnswer) {
  return axios.post(`${'add_answer'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    answer: inAnswer
  })
}

/**
 * Axios post request that sends the selected answer (rating for yellow-status inisghts) for an insight to the backend.
 * @param {String} inPaperId 
 * @param {String} inInsight 
 * @param {String} inAnswer 
 */
export function postRateAnswer (inPaperId, inInsight, inAnswer, inUpvote) {
  return axios.post(`${'rate_answer'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    answer: inAnswer,
    upvote: inUpvote
  })
}
/**
 * Axios post request that sends new insight added by the user to the backend.
 * @param {String} inPaperId 
 * @param {String} inInsight 
 * @param {String} inAnswer 
 */
export function postInsight (inPaperId, inInsight, inCategories) {
  return axios.post(`${'add_insight'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    categories: inCategories
  })
}

/**
 * Axios post request that sends current URL and recieves the .csv file with available insight data for direct-download.
 * @param {String} query
 */
export function fetchDownload (query) {
  return axios.post(`${'download'}`, {url: query}, {
    responseType: 'blob',
  })
}

/**
 * Axios post request that sends _Binder_ URL's to the backend for the multiple-paper direct-download.
 * @param {Array} binder
 */
export function postBinder(binder){
  return axios.post(`${'download'}`, {urls_from_binder: binder}, {
    responseType: 'blop',
  })
}
/**
 * Axios post request that sends insight-not-relevant error to the backend so it can be handled.
 * @param {String} inInsight
 * @param {Array} inCategories
 */
export function postInsightNotRelevant (inInsight, inCategories) {
  return axios.post(`${'insight_not_relevant_for_category'}`, {
    insight: inInsight,
    categories: inCategories
  })
}
/**
 * Axios post request that sends typo-error to the backend so it can be handled by downvoting it double.
 * @param {String} inInsight 
 */
export function postTypoError (inInsight) {
  return axios.post(`${'typo_error'}`, {
    insight: inInsight
  })
}
/**
 * Axios post request that sends request for topic related keywoards for the autocompleate feature.
 * @param {Array} inCategories 
 */
export function fetchAutocomplete (inCategories) {
  return axios.post(`${'autocomplete'}`, {categories: inCategories})
}



