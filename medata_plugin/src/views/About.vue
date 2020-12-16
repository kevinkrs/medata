<template>
<div class="container">
  <img src="../assets/medata_black.png" width="200">
  <div class="about">
      <h1>Welcome to Medata!</h1>
      <div v-if= "!valid">
        <button class ="mainButton" @click= 'checkURL()'>Check</button>
      </div>
      <div v-else>
        <router-link to = "/home"> 
        <button class ="mainButton" @click= 'startLoading()'>Load Data</button>
        </router-link>
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
        valid: false,
        substr: 'https://dl.acm.org/'
    }
  },
  computed: mapState({
    query: state => state.query
  }),

  methods: {
    checkURL() {
      var vm = this
      chrome.tabs.query({currentWindow: true, active: true}, 
          function (tabs){
          var querySub = tabs[0].url.substring(0, 19)
          if (querySub == vm.substr) { 
              alert('Valid URL found')
              vm.$store.dispatch('loadQuery', tabs[0].url)
              vm.valid = true}
          else {
            alert("You're currently not on dl.acm.org")
          }
      })
    },
    showURL (){
      alert(this.query)
    },
    startLoading (){
     this.$store.dispatch('loadMetadata')
    }
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