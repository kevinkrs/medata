
<template>
<div class ="extension">
  <div class="main-column">

    <!--Picture of the MEDATA logo-->
    <div class="headline">
      <button v-show="!legendVisible" style="display:inline" class="button-legend" @click="legendVisible = !legendVisible">
        <div><img class="img-button-legend" src="../assets/info.png" /></div>
      </button>
      <button v-show="legendVisible" style="display:none" class="button-legend2" @click="legendVisible = !legendVisible">
        <div><img class="img-button-legend" src="../assets/arrow-up.png" /></div>      
      </button>
      <img class="logo" src="../assets/medata_black.png" width="200"/> 
      <button class="insight-button-yellow">
        <img class="img-button" src="../assets/github.png" @click = "openGit"/>
      </button>
    </div>

    <fieldset v-show="legendVisible" style="display:none" class="grey-box-legend">
        <p> You can download all <b>available</b> insights of the collected papers from your binder by clicking on <i>Download Binder Insights</i></p>
    </fieldset>

    <div class= "download-binder">
        <button class="main-button" @click ='setBinder()'>Download Binder Insights</button>
    </div>
  </div>
</div>
  
</template>

<script>

export default {
   mounted () {
    browser.runtime.sendMessage({})
  },
  /**
   * Users can access a collapsable information box as on the other components. It is triggered inside the html with the boolean _legendVisible_. 
   */
    data () {
      return {
          legendVisible: false,
      }
    },

      methods: {
        /**
         * chrome extension call to _background.js_ for opening a new 
         */
        openGit () {
        chrome.tabs.create({url: "https://github.com"});
        },
      /**
         * To get all available data the backend needs all the paper urls from the binder. In order to get this information 
         * the _content-script.js_ of the chrome extension is triggered with _setBinder()_. 
         * There is a counterpart awaiting the call to provide the requested DOM elements. 
         * After sending the request the function awaits a response which is handled with the function bellow.
         *@class
         */
        setBinder() {
          var vm = this
            chrome.tabs.query({
            /**
             * Sends message to the _content-script.js_ to activate scraping for particular DOM elements.
             */
              active: true, currentWindow: true}, function(tabs){
                chrome.tabs.sendMessage(
                          tabs[0].id, 
                          {from: 'binder', subject:'getLinks'}, 
                          vm.sendBinder) 
                        }
              )},
            
         /**
          * The repsonse from the _content-script.js_ is handled inside here and first commited to a state object inside vuex store and aftewards 
          * dispatcht to the backend where the available data is bundled and sent back as direct download.
          */ 
        sendBinder(responseDom) {
          this.$store.dispatch('fetchBinder', responseDom)
          this.$store.dispatch('sendBinder')
          },

    }
}

</script>

<style>
.download-binder{
    margin-top: 50px;
    margin-bottom: 50px;

}

.main-button{
    border-radius: 6px;
    outline: none;
    border-style: none;
    width: 70%;
    height: 30px;
    color: white;
    background-color: #8F8F8F;
    margin-top: 10px;
  }

  .main-button:hover {
    background-color: #3a3a3a;
    color: white;
  }

.extension {
  box-sizing: border-box;
  width: 300px;
  padding-bottom: 10px;
  background-color:#ffffff;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 17px;
  color: #3A3A3A ;
}
.main-column{
  display: block;
  padding-top: 20px;
  padding-left: 10px;
  padding-right: 10px;

}
.headline {
  display: flex;
  justify-content: space-between;
  padding-left: 10px;
  padding-right: 10px;
}

.img-button {
    width: 150%;
    margin-left: -22%;
    margin-top: 5%;
  }

.img-button-legend {
    width: 27px;
    margin-left: -2.5px;
    margin-top: 3px;
  }

.insight-button-yellow {
   border: 0px;
   background-color: transparent;
   outline: none;
   width: 30px;
   height: 30px;
   float: right;
   border-radius: 5px;
}

.button-legend {
   border: 0px;
   background-color: #ffffff;
   outline: none;
   width: 50px;
   margin-left: -8px;
   margin-right: -12px;
   margin-top: -10px;
   height: 50px;
   float: right;
   border-radius: 5px 5px 0px 0px;  
   }

.button-legend2 {
   border: 0px;
   background-color: #f7f7f7;
   outline: none;
   width: 50px;
   margin-left: -8px;
   margin-right: -12px;
   margin-top: -10px;
   height: 50px;
   float: right;
   border-radius: 5px 5px 0px 0px;
   box-shadow: 3px 0px 0px silver;  
   }

   

.grey-box-legend {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  width: 91.5%;
  border: 0px;
  padding: 10px;
  margin-bottom: 20px;
  background-color: #f7f7f7;
  border-radius: 0px 5px 5px 5px;
  box-shadow: 3px 3px 3px silver;
}


.logo{
  margin-bottom: 15px;
  width: 50%;
}

</style>