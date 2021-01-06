<template>
<div class="container">
  <img src="../assets/medata_black.png" width="200">
  <div class="about">
      <h1>Welcome to Medata!</h1>
      <div>
        <button class ="mainButton" @click= 'checkURL()'>Load Data</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  // TODO URL to backend
  data()  {
    return{
        substr: 'https://dl.acm.org/',
        regex: /dl\.acm\.org\/doi\/\d+\.\d{3,}\//
    }
  },
  computed: mapState({
    query: state => state.query
  }),

  methods: {
    // With this method we check the current URL if it's on dl.acm.org. If so, we save the URl inside a state variable to submit it to the backend in order
    // to start the webscraper and search for the right category for providing the right data from our database
    checkURL() {
      // because of a function inside the function, we can't access data directly with "this". Hence we need this help-variable var vm = this
      var vm = this
      // Takes current chrome tab window
      chrome.tabs.query({currentWindow: true, active: true}, 
          function (tabs){
            //var regex = /dl\.acm\.org\/doi\/\d+\.\d{3,}\//
            var url = tabs[0].url
            var querySub = tabs[0].url.substring(0, 19)
            if (tabs[0].url.match(vm.regex)) { 
              // alert('Valid URL found')
              // if URL is a dl.acm.org URl we save it to our state 
              vm.$store.dispatch('loadQuery', tabs[0].url)
              .then(vm.$store.dispatch('loadMetadata'))
              // With router.push we can route to another url automatically
              vm.$router.push({path : '/home'})
          }
            else if(vm.substring == this.querySub) {
              alert("Please open a particular article to continue")
          }
          else {
              alert("You're currently not on the dl.acm.org website")
          }
      })
    },
  }
}
</script>

<style scoped>
.container {
  padding-top: 50px;
  box-sizing: border-box;
  background-color: lightgray;
  width: 300px;
}
.about {
  margin-top: 50px;
  padding-bottom: 50px;
  box-sizing: border-box;
  background-color: lightgray;
  
}
.mainButton{
  border-radius: 5px;
  width: 90px;
  height: 50px;
  color: white;
  background-color: rgb(41, 17, 160);
}

.mainButton:hover {
  background-color: rgb(182, 182, 182);
  border: 1px solid black;
}

h1 {
  font-size: 20px;
}
</style>