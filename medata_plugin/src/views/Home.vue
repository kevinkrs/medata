<template>
<div class = "extension">
  <div class="main-column">

    <!--Picture of the MEDATA logo-->
    <div class="headline">
      <button v-show="!legendVisible" style="display:inline" class="button-legend" @click="legendVisible = !legendVisible">
        <div><img class="img-button-legend" src="../assets/info.png" ></div>
      </button>
      <button v-show="legendVisible" style="display:none" class="button-legend2" @click="legendVisible = !legendVisible">
        <div><img class="img-button-legend" src="../assets/arrow-up.png" ></div>      
      </button>
      <img class="logo" src="../assets/medata_black.png" width="200"> 
      <button class="insight-button-yellow">
        <img class="img-button" src="../assets/github.png" @click = "openGit">
      </button>
    </div>
    
    <!--This fieldset element "grey-box" contains everything reagardin the legend-->
    <fieldset v-show="legendVisible" style="display:none" class="grey-box-legend">
      <!--The three div elements "grey-insight" represent the the three boxes/insights inside the legend-->
      <div class="grey-insight">
        <div class="grey-insight-name" @click="visible(-1)">confirmed insigth</div>
        <!--The div "grey-insight-button" contains the green/yellow or red button and the corresponding fold-out toggle box-->
        <div class="grey-insight-button">
          <button class="insight-button-green" @click="visible(-1)">
            <div id=-1001 style="display:inline"><img class="img-button" src="../assets/info-green.png" ></div>
            <div id=-2001 style="display:none"><img class="img-button" src="../assets/arrow-up-green.png" ></div>      
          </button>
          <div id=-1 style="display:none">
            <div class="grey-toggleBox">
              <p>The insights with a <b> green arrow </b> on the right are confirmed by <br> at <b> least 5 other </b> users. </p>
              <p> The confirmed value can be upvoted further to strengthen it's correctness as well as downvoted via an error reporting </p>
            </div>
          </div>
        </div>
      </div>
      <div class="grey-insight">
        <div class="grey-insight-name" @click="visible(-2)">validation needed</div>
        <div class="grey-insight-button">
          <button class="insight-button-yellow" @click="visible(-2)">
            <div id=-1002 style="display:inline"><img class="img-button" src="../assets/info-yellow.png" ></div>
            <div id=-2002 style="display:none"><img class="img-button" src="../assets/arrow-up-yellow.png" ></div>      
          </button>

          <div id=-2 style="display:none">
            <div class="grey-toggleBox">
              <p>The insights with a <b> yellow arrow </b> on the right contain values submitted by users that have to be confirmed by others. </p>
              <p>User can upvote an existing answers (by clicking on it) or submit their own in the input field below.</p>
              <p> After at least 5 upvotes by other users, the upvoted value is getting marked as confirmed and the insight changes from yellow status to green status.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="grey-insight">
        <div class="grey-insight-name" @click="visible(-3)">
          enter information
        </div>
        <div class="grey-insight-button">
          <button class="insight-button-red" @click="visible(-3)">
          <div id=-1003 style="display:inline"><img class="img-button" src="../assets/info-red.png" ></div>
          <div id=-2003 style="display:none"><img class="img-button" src="../assets/arrow-up-red.png" ></div>      
          </button>
          <div id=-3 style="display:none">
            <div class="grey-toggleBox">
              <p> The insights with a <b> red arrow </b> on the right contain no values yet. </p>
              <p> User can add values with the input field. After adding a value the insight is switching instantly from red status to yellow status. <br> 
              Now users can vote for an answer or add new answers. </p>
            </div>
          </div>
        </div>
      </div>
    </fieldset>

    <!--If backend has no information to given category it's responding with an empty list. Here we check if the list is truly empty.
    If it is, we display first the first div class "noData". If not empty we display second div -->
    <div v-if='metadata == null'>
      <div class="noData">
        <p> Sorry there is no data for this category available yet </p>
      </div>
    </div>
      
    <div v-else>
      <!--The div element "box 2" represents one insight listed under the legend and also consists of
      a short text and a colored box.-->
      <div class="insight" v-for="entry in metadata" :key="entry.id">
        <div class="insight-name">
          {{entry.name}}
        </div>
        <!--Each insight can have either a green, yellow or red button and the corresponding toggle box.
        An v-if will create these buttons colored red, yellow or green and the corresponding toggle box
        depending on whether the passed numerical value "confirmed" inside the "metadaata" array
        (recieved inside script from the store file)is 0,1 or something else.-->
        
      
        <div v-if='entry.answer.length == 0' class= "insight-button">
          <!--With a click on the colored button the function visable is called and the id of the insight
          is passed. This ensures that the corresponding toggle box becomes visible.-->
          <button class="insight-button-red" @click="visible(entry.id), saveInName(entry.name), sendInsightRelevance()">
            <div :id=entry.id-1000 style="display:inline"><img class="img-button" src="../assets/arrow-down-red.png" ></div>
            <div :id=entry.id-2000 style="display:none"><img class="img-button" src="../assets/arrow-up-red.png" ></div>      
          </button>

            <div :id=entry.id+1000 style="display:none">

              <!--The div "insight-name2" is only used so that the div "insight-toggleBox" has the right distance to the top depending on whether the name of the insight goes over one, two, three,... lines. In css the div "insight-name2" is made invisible again.-->
              <div class="insight-name2">
                {{entry.name}}
              </div>

              <div class="insight-toggleBox">
                <button class="error-button" @click="visible2(entry.id+1000)">back</button>
                <button id ="error1" class="error-button-2" @click='sendTypoError()'>Report typo </button> <br> 
                <button id ="error2" class="error-button-2" @click='sendInsightNotRelevantError()'>Report insignificance of this insight </button>
              </div>
            </div> 

          <div :id=entry.id style="display:none">

            <!--The div "insight-name2" is only used so that the div "insight-toggleBox" has the right distance to the top depending on whether the name of the insight goes over one, two, three,... lines. In css the div "insight-name2" is made invisible again.-->
            <div class="insight-name2">
              {{entry.name}}
            </div>

            <div class="insight-toggleBox">
              <button class="error-button" @click="visible2(entry.id+1000)">report error</button>
              <div class="insight-add">
                <p>Please enter information:</p>
                <input class="inputfield" v-model='userInput' @keyup.enter='saveUserInput(), sendUserAnswer()'><br>
                <button class="main-button" @click="saveUserInput(), sendUserAnswer()">Submit</button>
              </div>
            </div>
          </div>
        </div>
        <div div v-else-if="entry.answer[0].answer_score < 3" class="insight-button">
          <button class="insight-button-yellow" @click="visible(entry.id), saveInName(entry.name), sendInsightRelevance()">
            <div :id=entry.id-1000 style="display:inline"><img class="img-button" src="../assets/arrow-down-yellow.png" ></div>
            <div :id=entry.id-2000 style="display:none"><img class="img-button" src="../assets/arrow-up-yellow.png" ></div>
          </button>

            <div :id=entry.id+1000 style="display:none">

              <!--The div "insight-name2" is only used so that the div "insight-toggleBox" has the right distance to the top depending on whether the name of the insight goes over one, two, three,... lines. In css the div "insight-name2" is made invisible again.-->
              <div class="insight-name2">
                {{entry.name}}
              </div>

              <div class="insight-toggleBox">
                <button class="error-button" @click="visible2(entry.id+1000)">back</button>
                <button id ="error1" class="error-button-2" @click='sendTypoError()'>Report typo </button> <br> 
                <button id ="error2" class="error-button-2" @click='sendInsightNotRelevantError()'>Report insignificance of this insight </button>
              </div>
            </div> 

          <div :id=entry.id style="display:none">

            <!--The div "insight-name2" is only used so that the div "insight-toggleBox" has the right distance to the top depending on whether the name of the insight goes over one, two, three,... lines. In css the div "insight-name2" is made invisible again.-->
            <div class="insight-name2">
              {{entry.name}}
            </div>

            <div class="insight-toggleBox">
          
            <button class="error-button" @click="visible2(entry.id+1000)">report error</button>
              <div class="insight-answers">
                <p>Please select <br> the correct Answer</p>

               <div class="row">
                    <div v-for="answer in entry.answer" :key ="answer">
                     
                      <button type="button"  class="answer-button" @click="saveAnswerSelection(answer.answer), sendAnswerSelection()">
                        {{answer.answer}}
                      </button>
                    </div>
                </div>

              </div>
              <div class="insight-add">
                <p>Add value:</p>
                <input class="inputfield" v-model='userInput' @keyup.enter='saveUserInput(), sendUserAnswer()'><br>
                <button class="main-button" @click="saveUserInput(), sendUserAnswer()">Submit</button>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="insight-button">
          <button class="insight-button-green" @click="visible(entry.id), saveInName(entry.name), sendInsightRelevance(), saveAnswerSelection(entry.answer[0].answer)">
            <div :id=entry.id-1000 style="display:inline"><img class="img-button" src="../assets/arrow-down-green.png" ></div>
            <div :id=entry.id-2000 style="display:none"><img class="img-button" src="../assets/arrow-up-green.png" ></div>
          </button>

            <div :id=entry.id+1000 style="display:none">

              <!--The div "insight-name2" is only used so that the div "insight-toggleBox" has the right distance to the top depending on whether the name of the insight goes over one, two, three,... lines. In css the div "insight-name2" is made invisible again.-->
              <div class="insight-name2">
                {{entry.name}}
              </div>

              <div class="insight-toggleBox">
                <button class="error-button" @click="visible2(entry.id+1000)">back</button>
                 <button id ="error1" class="error-button-2" @click='sendTypoError()'>Report typo </button> <br> 
                <button id ="error2" class="error-button-2" @click='sendValueError()'>Report incorrect value </button>
              </div>
            </div> 

          <div :id=entry.id style="display:none">

            <!--The div "insight-name2" is only used so that the div "insight-toggleBox" has the right distance to the top depending on whether the name of the insight goes over one, two, three,... lines. In css the div "insight-name2" is made invisible again.-->
            <div class="insight-name2">
              {{entry.name}}
            </div>

            <div class="insight-toggleBox">
            <button class="error-button" @click="visible2(entry.id+1000)">report error</button>
            
                <p class="insight-green-answer">{{entry.answer[0].answer}} <br></p>
                <div class="insight-green">
                  <div class="insight-green-text">
                    <p> Number of<br> confirmations </p>
                  </div>
                  <div class="insight-green-line"></div>
                  <div class="insight-green-number">
                    <p>{{entry.answer[0].answer_score}}</p>                   
                  </div>
                </div>
                <button class="green-button" @click='sendAnswerSelection()'>Confirm</button>
            </div>
          </div>
        </div>
      </div>

      <div><br></div>

      <!--This fieldset element "grey-box" contains everything reagardin the "more-functions"-->
      <fieldset class="grey-box">
        <!--The three div elements "box-1-content" represent the the three elements inside the legend.
        Each element consists of a short text and a colored box-->
        <div class="grey-insight">
          <div class="grey-insight-name">
            download insights
          </div>
          <div class="grey-insight-button">
            <button class="insight-button-yellow" @click="sendDownloadRequest()"><img class="img-button" src="../assets/direct-download.png" ></button>
          </div>
        </div>
        <div class="grey-insight">
          <div class="grey-insight-name">
            add relevant insight
          </div>
          <div class="grey-insight-button">
            <button class="insight-button-yellow" @click="visible(-5)">
            <div id=-1005 style="display:inline"><img class="img-button" src="../assets/add.png" ></div>
            <div id=-2005 style="display:none"><img class="img-button" src="../assets/arrow-up.png" ></div>      
            </button>
            <div id=-5 style="display:none">
              <div class="new-insight-toggleBox">
                <input class="inputfield2" type="text" autocomplete="off" @keyup.enter='saveUserInput(), sendUserInsight()' @input = "filterParameters" v-model="userInput" @focus = "modal = true"/>
                <div v-if="filtered && modal">
                  <ul>
                    <li class = "autocomplete" v-for="param in filtered" :key = "param"  @click = "setParam(param)">
                      {{param}}
                    </li>
                  </ul>
                </div>
                <div class="insight-add">
                  <button class="main-button" @click="saveUserInput(), sendUserInsight()">Save</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </fieldset>

    </div>
  </div> 
</div>
</template>

<script>
// mapState is a function, that maintains a reference to a specific property of the "state" object (state.metadata)
// if the property is mutated, a component using mapState will react to that change and refresh the UI that is tied to this data
import {mapState} from 'vuex'

export default {
  name: 'main',
  data () {
    return {
    // Empty String for possible user input
      userInput: '',
      legendVisible: false,
      // TODO: Backend has to send an array with common words for certain category 
      filtered: [],
      modal: false
    }
  },
  methods: {
    // Function only for testing
    openGit () {
      chrome.tabs.create({url: "https://github.com"});
    },

    filterParameters() {
      if (this.userInput.length == 0){
        this.filtered = []
      }
      else{
        this.filtered = this.autocomplete.filter(userInput =>{
          return userInput.toLowerCase().startsWith(this.userInput.toLowerCase())
        })
      }
    },
    setParam(param) {
      this.userInput = param
      this.modal = false
    },
    // TODO commments
    visible: function (divId) {
      /*The for loop closes all divs to ensure that only one div is open at a time*/
      for (var i = -10000; i <= 10000; i++) {
        if (document.getElementById(i) != null && i != divId && i != -6){
        document.getElementById(i).style.display = 'none';
        }                
      }
      if (document.getElementById(divId).style.display === 'none') {
        document.getElementById(divId).style.display = 'inline';
        document.getElementById(divId-1000).style.display = 'none';
        document.getElementById(divId-2000).style.display = 'inline';
      } else {
        document.getElementById(divId).style.display = 'none';
        document.getElementById(divId-1000).style.display = 'inline';
        document.getElementById(divId-2000).style.display = 'none';
      }

      for (var i = -1010; i <= -10; i++) {
        if (document.getElementById(i) != null && i != (divId-1000)){
        document.getElementById(i).style.display = 'inline';
        }                
      }
    },

    visible2: function (divId) {
      if (document.getElementById(divId).style.display === 'none') {
        document.getElementById(divId).style.display = 'inline';
        document.getElementById(divId-1000).style.display = 'none';
      } else {
        document.getElementById(divId).style.display = 'none';
        document.getElementById(divId-1000).style.display = 'inline';
      }
    },

    visible3: function (divId) {
        document.getElementById(divId+100000).style.display = 'none';
        document.getElementById(divId+200000).style.display = 'inline';    
    },
    // All the following methods are merely for saving data as state objects
    saveInName(name) {
      this.$store.dispatch('fetchInName', name)
    },
    saveAnswerSelection(answer) {
      this.$store.dispatch('fetchUserAnswer', answer) 
    },
    // TODO: This method saves & sends user Input 
    saveUserInput() {
      if (this.userInput == ''){
        alert('Please enter some data before submitting!')
      }
      else{
         this.$store.dispatch('fetchUserInput', this.userInput)
      }
    },
    // Yellow status for rating answers
    sendAnswerSelection() {
      this.$store.dispatch('sendRateAnswer')
      alert('Thanks for rating!')
      this.$store.dispatch('loadMetadata')
    },
    // For new answers by user
    sendUserAnswer() {
      if (this.currentUserInput == ''){
        console.log('empty userInput')
      }
      else{
        this.$store.dispatch('sendAnswer')
        alert('Thanks for submitting!')
        this.userInput = ''
        this.$store.dispatch('loadMetadata')
        }
    },
    // For new insights by user
    sendUserInsight() {
      if(this.currentUserInput == ''){
        console.log('empty userInput')
      }
      else{
      this.$store.dispatch('sendInsight')
      alert('Thanks for submitting!')
      this.userInput = ''
      this.$store.dispatch('loadMetadata')
      }
    },
  
    sendDownloadRequest() {
      this.$store.dispatch("loadDownload")
    },
  
    // User sends relevance of insight (upvote) on insight click
    sendInsightRelevance(){
      this.$store.dispatch('sendRateRelevanceInsight')
      //this.$store.dispatch('loadMetadata')
    },

    sendInsightNotRelevantError() {
      this.$store.dispatch('sendInsightNotRelevantError')
      this.$store.dispatch('loadMetadata')
      alert('Thank you for reporting! If more user report this insight as insignificant it will be deleted.')
    },
    sendValueError() {
      this.$store.dispatch('sendValueError')
      this.$store.dispatch('loadMetadata')
      alert("Thank you for reporting! The value is going to be checked.")
    },
     sendTypoError() {
        this.$store.dispatch('sendTypoError')
        this.$store.dispatch('loadMetadata')
        alert('Thank you for reporting typo. Our team is going to check your reported typo.')
     },
     sendScraper() {
       this.$store.dispatch('loadFurtherInformation')
     }

  },
  // mapstate is a Vuex component (using computed) summarizing the command of this.$store.state.metadata
  // we can easily load all our state objects inside our Home-Component and access it by calling this."propertyname"
  computed: {
    ...mapState([
        'metadata', 
        'currentIn',
        'currentAnswer',
        'currentUserInput',
        'selectedError',
        'currentCategories',
        'autocomplete'
    ]),

  },
  created: 
      function () {
          this.sendScraper()
        
  }

}
</script>

<style scoped>

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

.logo{
  margin-bottom: 15px;
  width: 50%;
}

/*grey- | design for "Legend" and "more functions"*/
 .grey-box {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    border: 0px;
    padding: 10px;
    margin-bottom: 20px;
    background-color: #f7f7f7;
    border-radius: 5px 5px 5px 5px;
    box-shadow: 3px 3px 3px silver;
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

  .grey-insight {
    display: flex;
    justify-content: space-between;
    padding-top: 5px;
    padding-bottom: 5px;
  }

  .grey-insight-name {
    width: 80%;
    height: 30px;
    padding: 8px;
    text-align: left;
    background-color:  #FFFFFF ;
    border-radius: 5px 0px 0px 5px;
  }

  .grey-insight-button {
    width: 20%;
    padding: 8px;
    background-color: #FFFFFF ;
    border-radius: 0px 5px 5px 0px;
  }

  .grey-toggleBox {
  text-align: left;
  padding: 8px;
  font-size: 85%;
  margin-top: 30px;
  margin-left: -384%;
  margin-right: -8px;
  margin-bottom: -8px;
  border-radius: 0px 0px 5px 5px;
  background-color: #FFFFFF;
  }

  .new-insight-toggleBox {
  text-align: center;
  padding: 8px;
  font-size: 85%;
  margin-top: 30px;
  margin-left: -384%;
  margin-right: -8px;
  margin-bottom: -8px;
  border-radius: 0px 0px 5px 5px;
  background-color: #FFFFFF;
  }

/*insight- | desgin for the list of insights*/
  .insight {
    display: flex;
    justify-content: space-between;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 2px;
    padding-right: 2px;
  }

  .insight-name {
    width: 80%;
    padding: 8px;
    text-align: left;
    background-color: #f7f7f7;
    box-shadow: 3px 3px 3px silver;
    border-radius: 5px 0px 0px 5px;
  }
  .insight-name2 {
    width: 350%;
    padding: 8px;
    color: transparent;
    margin-top: -8px;
    margin-left: -384%;
    margin-right: -8px;
    text-align: left;
    background-color: transparent;
    border-radius: 5px 0px 0px 5px;
  }

  .insight-button {
    width: 20%;
    padding: 8px;
    background-color: #f7f7f7;
    box-shadow: 3px 3px 3px silver;
    border-radius: 0px 5px 5px 0px;
  }

 .insight-button-green {
   border: 0px;
   background-color: transparent;
   outline: none;
   width: 30px;
   height: 30px;
   float: right;
   border-radius: 5px;
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
  .insight-button-red {
   border: 0px;
   background-color: transparent;
   outline: none;
   width: 30px;
   height: 30px;
   float: right;
   font-weight: bold;
   border-radius: 5px;
 }

  .insight-button:focus{
    width: 60px;
  }

  .insight-toggleBox {
    background-color:#f7f7f7;
    text-align: center;
    font-size: 85%;
    padding: 10px;
    margin-top: 0px;
    margin-left: -384%;
    margin-right: -8px;
    margin-bottom: -8px;
    border-radius: 0px 0px 5px 5px;
    box-shadow: 3px 3px 3px silver;
  }

  .insight-green-answer {
  font-size: 25px;
  font-weight: bold;
  margin-top: 15px;
  margin-bottom: 5px;
  }

  .insight-green {
    display: flex;
    justify-content: center;
    margin-left: -60px;
  }

  .insight-green-text {
    text-align: right;
  }

  .insight-green-line {
    border-left: 1.5px black solid ;
    width: 0px;
    height: 35px;
    margin-left: 5px;
    margin-top: 17px;
  }

  .insight-green-number {
    text-align: right;
    font-size: 25px;
    height: 20px;
    margin-left: 5px;
    margin-top: -8px;
  }

/* -button | design for buttons*/
  .main-button{
    border-radius: 6px;
    outline: none;
    border-style: none;
    width: 80px;
    height: 30px;
    color: white;
    background-color: #8F8F8F;
    margin-top: 10px;
  }

  .main-button:hover {
    background-color: #3a3a3a;
    color: white;
  }

  .main-button-clicked{
    border-radius: 6px;
    outline: none;
    border-style: none;
    width: 80px;
    height: 30px;
    color: white;
    background-color: #8F8F8F;
    margin-top: 10px;
  }

  .inputfield {
    border-radius: 6px;
  }

  .inputfield2 {
    border-radius: 6px;
    width: 140px;
    margin-top: 10px;
    margin-bottom: 0px;
  }

  .report-button {
    margin: 15px;
    border: none;
    color: rgb(235, 235, 235);
    background: rgb(186, 15, 15);
    border-radius: 5px;
    width: 70px;
    height: 30px;
  }

  .report-button:hover { 
    color: black;
    background: rgb(184, 184, 184);
  }

  .answer-button {
    border-radius: 6px;
    outline: none;
    border-style: none;
    width: 70%;
    padding: 7px;
    background-color: #FFD700;
    margin-top: 10px;
  }

  .answer-button:hover {
    background-color: #3a3a3a;
    color: white;
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
  
  .img-button-legend {
    width: 27px;
    margin-left: -2.5px;
    margin-top: 3px;
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

  .img-button {
    width: 150%;
    margin-left: -22%;
    margin-top: 5%;
  }

  .error-button {
    float: left;
    font-size: 65%;
    width: 25%;
    margin-bottom: 10px;
    margin-top: -10px;
    border-radius: 4px;
    outline: none;
    border-style: none;
    color: white;
    background-color: #8F8F8F;
  }

  .error-button:hover { 
    background-color: #3a3a3a;
    color: white;
  }
  
  .error-button-2 {
    width: 80%;
    outline: none;
    padding: 4px;
    border-style: none;
    color: white;
    background-color: #CD0000;
    border-radius: 6px;
    margin-bottom: 10px;
  }

  .error-button-2:hover {
    background-color: #3a3a3a;
    color: white;
  }

  .green-button {
    border-radius: 6px;
    outline: none;
    border-style: none;
    width: 80px;
    height: 30px;
    color: white;
    background-color: #008D09;
  }

  .green-button:hover {
    background-color: #3a3a3a;
    color: white;
  }

  .green-button-clicked {
    border-radius: 6px;
    outline: none;
    border-style: none;
    width: 80px;
    height: 30px;
    color: white;
    background-color: #8F8F8F;
  }

.noData{
  display: block;
  margin-top: 30px;
  padding-left: 10px;
  padding-right: 10px;
  margin-left: auto;
  margin-right: auto;
  height: 100px;
  border-radius: 5px;
  background-color: white;
  border: 1px solid white
}

.downloadPNG {
  width: 10%;
  margin-bottom: -5px;
}

ul {
  display: flex;
  flex-wrap: wrap;
  list-style-type: none;
  margin-top: 0px;
  margin-left: 5px;
  }

li {
  border-bottom: 0.5px solid rgb(120, 120, 120);
  border-left: 0.5px solid rgb(120, 120, 120);
  border-right: 0.5px solid rgb(120, 120, 120);
  border-radius: 5px, 0px, 0px, 0px;
  background-color: lightblue;
  width: 65%;
  padding: 10px;
  font-size: 15px;
}
li:hover {
  border: 1px, solid rgb(120, 120, 120);
  background-color: rgb(33, 179, 228);
}

</style>