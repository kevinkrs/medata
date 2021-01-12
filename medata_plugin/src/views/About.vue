<template>
<div class="container">
  <img src="../assets/medata_black.png" width="200">
  <div class="about">
       <div v-if = 'button'>
        <button class ="mainButton" @click='checkURL()'>Load Data</button>
      </div>
      <div v-else>
       <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
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
        regex: /dl\.acm\.org\/doi\/\d+\.\d{3,}\//,
        button: true
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
            var querySub = tabs[0].url.substring(0, 19)
            if (tabs[0].url.match(vm.regex)) { 
              vm.button = false
              // alert('Valid URL found')
              // if URL is a dl.acm.org URl we save it to our state 
              vm.$store.dispatch('loadQuery', tabs[0].url)
              .then(vm.loadData())
              // With router.push we can route to another url automatically 
          }
            else if(querySub == vm.substr) {
              alert("Please open a particular article to continue")
          }
            else {
              alert("You're currently not on the dl.acm.org website")
          }
      })
    },
    // This function is called by checkURL(). After dispatching for "loadMetadata" and resolving it, the route is getting pushed to our main page 
    // with all the data already loaded
    async loadData(){
      await this.$store.dispatch('loadMetadata')
      await this.$router.push('/home')
    },
  }
}
</script>


<style scoped>
.container {
  padding-top: 50px;
  box-sizing: border-box;
  background-color: #ffffff;
  width: 300px;
}
.about {
  margin-top: 50px;
  padding-bottom: 50px;
  box-sizing: border-box;
  
}
.mainButton{
  border-radius: 5px;
  outline: none;
  border-style: none;
  width: 90px;
  height: 40px;
  color: white;
  background-color: #8F8F8F;
  }

.mainButton:hover {
  background-color: #3a3a3a;
  color: white;
}

h1 {
  font-size: 20px;
}

.lds-roller {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-roller div {
  animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  transform-origin: 40px 40px;
}
.lds-roller div:after {
  content: " ";
  display: block;
  position: absolute;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #3a3a3a;
  margin: -4px 0 0 -4px;
}
.lds-roller div:nth-child(1) {
  animation-delay: -0.036s;
}
.lds-roller div:nth-child(1):after {
  top: 63px;
  left: 63px;
}
.lds-roller div:nth-child(2) {
  animation-delay: -0.072s;
}
.lds-roller div:nth-child(2):after {
  top: 68px;
  left: 56px;
}
.lds-roller div:nth-child(3) {
  animation-delay: -0.108s;
}
.lds-roller div:nth-child(3):after {
  top: 71px;
  left: 48px;
}
.lds-roller div:nth-child(4) {
  animation-delay: -0.144s;
}
.lds-roller div:nth-child(4):after {
  top: 72px;
  left: 40px;
}
.lds-roller div:nth-child(5) {
  animation-delay: -0.18s;
}
.lds-roller div:nth-child(5):after {
  top: 71px;
  left: 32px;
}
.lds-roller div:nth-child(6) {
  animation-delay: -0.216s;
}
.lds-roller div:nth-child(6):after {
  top: 68px;
  left: 24px;
}
.lds-roller div:nth-child(7) {
  animation-delay: -0.252s;
}
.lds-roller div:nth-child(7):after {
  top: 63px;
  left: 17px;
}
.lds-roller div:nth-child(8) {
  animation-delay: -0.288s;
}
.lds-roller div:nth-child(8):after {
  top: 56px;
  left: 12px;
}
@keyframes lds-roller {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

</style>