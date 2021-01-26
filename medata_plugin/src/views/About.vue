<template>
<div class="container">
  <img src="../assets/medata_black.png" width="200">
  <div class="about">
       <div v-if = "status == 2">
        <p class ="info"> You're currently not visiting <br> <a href= "https://dl.acm.org/"> <i>dl.acm.org</i></a></p>
      </div>
      <div v-else-if = "status == 1">
         <p class ="info"> Please open an <a href= "https://dl.acm.org/"> <i>dl.acm.org</i></a><br> articel or paper to continue </p>
      </div>
      <div v-else-if = "status == 3">
         <p class ="info"> Please select a certain Binder to continue </p>
      </div>
      <div v-else>
       <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
      <div>
        <p> Loading data... </p>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {

  data()  {
    return{
        substr: /dl\.acm\.org\//,
        regex: /dl\.acm\.org\/doi\/((fullHtml\/)|(epdf\/)|(pdf\/)){0,1}\d+\.\d{3,}\//,
        regexBinder: /dl\.acm\.org\/action\/showBinder\?/,
        readingList: /dl\.acm\.org\/action\/showMyBinders/,
        status: 0
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
            if (tabs[0].url.match(vm.regex)) { 
              vm.status = 0
              // alert('Valid URL found')
              // if URL is a dl.acm.org URl we save it to our state 
              vm.$store.dispatch('loadQuery', tabs[0].url)
              .then(vm.loadData())
              // With router.push we can route to another url automatically 
          }
            else if(tabs[0].url.match(vm.regexBinder)){
              vm.$store.dispatch('loadQuery', tabs[0].url)
              vm.$router.push('/binder')
          }
           else if(tabs[0].url.match(vm.readingList)){
              vm.status = 3
            }
            else if(tabs[0].url.match(vm.substr)) {
              vm.status = 1
         
          }
            else {
              vm.status = 2
             
          }
      })
    },
    // This function is called by checkURL(). After dispatching for "loadMetadata" and resolving it, the route is getting pushed to our main page 
    // with all the data already loaded
    async loadData(){
      await this.$store.dispatch('loadMetadata')
      this.$store.dispatch('loadAutocomplete')
      await this.$router.push('/home')
    },
  },

    created: 
      function() {
        this.checkURL()
      },
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
.info {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 17px;
  color: #3A3A3A ;
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