import axios from 'axios'



// Query by user is send to backend
axios.defaults.baseURL = 'http://127.0.0.1:5000/'

axios.defaults.headers.common ['Content-Type']= 'application/json'

// Query by user is send to backend
export function fetchMetadata (query) {
  return axios.post(`${'get_specific'}`, {url: query})
}

export function fetchCategories(query) {
  return axios.post(`${'get_categories'}`, {url: query})
}

export function postRateRelevanceInsight (inPaperId, inInsight, inUpvote) {
  return axios.post(`${'rate_relevance_insight'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    upvote: inUpvote
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

// Function for the userInput of new relevant metadata
export function postInsight (inPaperId, inInsight, inCategories) {
  return axios.post(`${'add_insight'}`, {
    paper_id: inPaperId,
    insight: inInsight,
    categories: inCategories
  })
}

export function fetchDownload (query) {
  return axios.post(`${'download'}`, {url: query}, {
    responseType: 'blob',
  })
}

export function postInsightNotRelevant (inInsight, inCategories) {
  return axios.post(`${'insight_not_relevant_for_category'}`, {
    insight: inInsight,
    categories: inCategories
  })
}

export function postTypeError (inInsight) {
  return axios.post(`${'type_error'}`, {
    insight: inInsight
  })
}



