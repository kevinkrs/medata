/* eslint-disable no-template-curly-in-string */
import axios from 'axios'



// Query by user is send to backend
axios.defaults.baseURL = 'http://127.0.0.1:5000/'
// Doesn't work
axios.defaults.headers.common ['Content-Type']= 'application/json'

// Query by user is send to backend
export function fetchMetadata (query) {
  return axios.get(`${'get_specific'}`, {url: query})
}

// Function for the userInput of new relevant metadata
export function postInsight (inPaperId, inInsight, inCategories) {
  return axios.post(`${'add_insight'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    categories: inCategories
  })
}

export function postAnswer (inPaperId, inInsight, inAnswer) {
  return axios.post(`${'add_answer'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    answer: inAnswer
  })
}

export function postRateAnswer (inPaperId, inInsight, inAnswer, inUpvote) {
  return axios.post(`${'rate_answer'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    answer: inAnswer,
    upvote: inUpvote
  })
}

export function postRateRelevanceInsight (inPaperId, inInsight, inUpvote) {
  return axios.post(`${'rate_relevance_insight'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    upvote: inUpvote
  })
}
