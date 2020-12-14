/* eslint-disable no-template-curly-in-string */
import axios from 'axios'

/*
// Mock Data
const metadata = [{
    id: 1,
    name: 'Accuracy',
    value: '84%',
    upvotes: 0 // not confirmed = red
  },
  {
    id: 2,
    name: 'Recall',
    value: '91%',
    upvotes: 3 // validation needed = yellow
  },
  {
    id: 3,
    name: 'F1',
    value: '87%',
    upvotes: 10 // confirmed = green
  }]
  
  export function fetchMetadata () {
    return new Promise((resolve, reject) => {
      setTimeout(() => { resolve(metadata) }, 300)
    })
  }*/
  



// API URL from backend
axios.defaults.baseURL = 'http://127.0.0.1:5000/'

// Query by user is send to backend
export function fetchMetadata (url) {
  const inputUrl1 = url
  const inputUrl = "https://dl.acm.org/doi/10.1145/3360601"
  return axios.post(`${'get_specific'}`, {url: inputUrl})
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
