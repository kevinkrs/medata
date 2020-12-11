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
const API_URL = 'http://127.0.0.1:5000/'

// Query by user is send to backend
export function fetchMetadata () {
  return axios.get(`${API_URL}/get_specific`)
}

// Function for the user interaction with existing inightsexport function saveResponse (questionResponse) {
export function setResponse () {  
return axios.put(`${API_URL}/metadata/${questionResponse.id}`, questionResponse)
}

// Function for the userInput of new relevant metadata
export function postUserInput (userInput) {
  return axios.post(`${API_URL}/metadata/`, userInput)
}