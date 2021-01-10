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
      <a href="https://git.scc.kit.edu/issd/students/teamproject/ws20-il">
      <button class="insight-button-yellow">
        <img class="img-button" src="../assets/github.png" >
      </button></a>
    </div>
    
    <!--This fieldset element "grey-box" contains everything reagardin the legend-->
    <fieldset v-show="legendVisible" style="display:none" class="grey-box-legend">
      <!--The three div elements "grey-insight" represent the the three boxes/insights inside the legend-->
      <div class="grey-insight">
        <div class="grey-insight-name">confirmed insigth</div>
        <!--The div "grey-insight-button" contains the green/yellow or red button and the corresponding fold-out toggle box-->
        <div class="grey-insight-button">
          <button class="insight-button-green" @click="visible(-1)">
            <div id=-1001 style="display:inline"><img class="img-button" src="../assets/info-green.png" ></div>
            <div id=-2001 style="display:none"><img class="img-button" src="../assets/arrow-up-green.png" ></div>      
          </button>
          <div id=-1 style="display:none">
            <div class="grey-toggleBox">
              <p>Detailed explanation of a green insight</p>
            </div>
          </div>
        </div>
      </div>
      <div class="grey-insight">
        <div class="grey-insight-name">validation needed</div>
        <div class="grey-insight-button">
          <button class="insight-button-yellow" @click="visible(-2)">
            <div id=-1002 style="display:inline"><img class="img-button" src="../assets/info-yellow.png" ></div>
            <div id=-2002 style="display:none"><img class="img-button" src="../assets/arrow-up-yellow.png" ></div>      
          </button>
          <div id=-2 style="display:none">
            <div class="grey-toggleBox">
              <p>Detailed explanation of a yellow insight </p>
            </div>
          </div>
        </div>
      </div>
      <div class="grey-insight">
        <div class="grey-insight-name">
          enter information
        </div>
        <div class="grey-insight-button">
          <button class="insight-button-red" @click="visible(-3)">
          <div id=-1003 style="display:inline"><img class="img-button" src="../assets/info-red.png" ></div>
          <div id=-2003 style="display:none"><img class="img-button" src="../assets/arrow-up-red.png" ></div>      
          </button>
          <div id=-3 style="display:none">
            <div class="grey-toggleBox">
              <p>Detailed explanation of a red insight </p>
            </div>
          </div>
        </div>
      </div>
    </fieldset>

    <!--If backend has no information to given category it's responding with an empty list. Here we check if the list is truly empty.
    If it is, we display first the first div class "noData". If not empty we display second div -->
    <div v-if='metadata.length == 0'>
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
        
        <!--TODO insigth_upvores is not the right variable for comparision
        entry.answer.length == 0 -->
        <div v-if='entry.answer.length == 0' class= "insight-button">
          <!--With a click on the colored button the function visable is called and the id of the insight
          is passed. This ensures that the corresponding toggle box becomes visible.-->
          <button class="insight-button-red" @click="visible(entry.id), saveInName(entry.name), sendInsightRelevance()">
            <div :id=entry.id-1000 style="display:inline"><img class="img-button" src="../assets/arrow-down-red.png" ></div>
            <div :id=entry.id-2000 style="display:none"><img class="img-button" src="../assets/arrow-up-red.png" ></div>      
          </button>

            <div :id=entry.id+1000 style="display:none">
              <div class="insight-toggleBox">
                <button class="error-button" @click="visible2(entry.id+1000)">back</button>
                <button id ="error1" class="error-button-2" @click='saveSelectedError("type_error"), sendTypeError()'>Type Error</button> <br> 
                <button id ="error2" class="error-button-2" @click='saveSelectedError("relevance_error"), sendInsightNotRelevantError()'>Insight not relevant for this paper for this paper</button>
              </div>
            </div> 

          <div :id=entry.id style="display:none">
            <!--The div elements toggle-box-red/yellow/green define the frame of the three different
            toggle boxes-->
            <div class="insight-toggleBox">
              <button class="error-button" @click="visible2(entry.id+1000)">report an error</button>
              <p>Please enter information:</p>
                <!--TODO: implement button styles in CSS file-->
              <input placeholder="your relevant data" v-model='userInput' @keyup.enter='saveUserInput(), sendUserAnswer()'><br>
              <button class="submit-insight" @click="saveUserInput(), sendUserAnswer()">Submit</button>
            </div>
          </div>

        </div>
        <div div v-else-if="entry.answer[0].answer_score < 3" class="insight-button">
          <button class="insight-button-green" @click="visible(entry.id), saveInName(entry.name), sendInsightRelevance()">
            <div :id=entry.id-1000 style="display:inline"><img class="img-button" src="../assets/arrow-down-yellow.png" ></div>
            <div :id=entry.id-2000 style="display:none"><img class="img-button" src="../assets/arrow-up-yellow.png" ></div>
          </button>

            <div :id=entry.id+1000 style="display:none">
              <div class="insight-toggleBox">
                <button class="error-button" @click="visible2(entry.id+1000)">back</button>
                <button id ="error1" class="error-button-2" @click='saveSelectedError("type_error"),sendTypeError()'>Type Error</button> <br> 
                <button id ="error2" class="error-button-2" @click='saveSelectedError("relevance_error"), sendInsightNotRelevantError()'>Insight not relevant for this paper</button>
              </div>
            </div> 

          <div :id=entry.id style="display:none">
            <div class="insight-toggleBox">
              <!--STYLING TODO-->
            <button class="error-button" @click="visible2(entry.id+1000)">report an error</button>
              <div class="insight-answers">
                <p>Please select <br> the correct Answer</p>
               <div class="row">
                    <div v-for="answer in entry.answer" :key ="answer">
                      <!--How can i connect v-model directly -->
                      <button type="button"  class="answer-button" @click="saveAnswerSelection(answer.answer), sendAnswerSelection()">
                        {{answer.answer}}
                      </button>
                    </div>
                  </div>
              </div>
              <br>
              <p> Add value </p>
                <input class="userInput" v-model="userInput" @keyup.enter='saveUserInput(), sendUserAnswer()'> 
                <button class="submit-insight" @click="saveUserInput(), sendUserAnswer()">Submit</button>
            </div>
          </div>
        </div>
        <div v-else class="insight-button">
          <button class="insight-button-green" @click="visible(entry.id), saveInName(entry.name), sendInsightRelevance(), saveAnswerSelection(entry.answer[0].answer)">
            <div :id=entry.id-1000 style="display:inline"><img class="img-button" src="../assets/arrow-down-green.png" ></div>
            <div :id=entry.id-2000 style="display:none"><img class="img-button" src="../assets/arrow-up-green.png" ></div>
          </button>

            <div :id=entry.id+1000 style="display:none">
              <div class="insight-toggleBox">
                <button class="error-button" @click="visible2(entry.id+1000)">back</button>
                 <button id ="error1" class="error-button-2" @click='saveSelectedError("type_error"),sendTypeError()'>Type Error</button> <br> 
                <button id ="error2" class="error-button-2" @click='saveSelectedError("value_error"), sendValueError()'>Value Error</button>
              </div>
            </div> 

          <div :id=entry.id style="display:none">
            <div class="insight-toggleBox">
            <button class="error-button" @click="visible2(entry.id+1000)">report an error</button>
              <!--If function, for checking if the answer has highest upvotes-->
                <p class="displayAnswer">{{entry.answer[0].answer}} <br></p>
                <p> {{entry.answer[0].answer_upvotes}} users confirmed <br>
                    this information <br>
                </p>
              <button class="submit-button" @click='sendAnswerSelection()'>confirm</button>
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
            <button class="grey-button" @click="sendDownloadRequest()">
            <div id=-1004 style="display:inline"><img class="img-button" src="../assets/direct-download.png" ></div>
            <div id=-2004 style="display:none"><img class="img-button" src="../assets/arrow-up.png" ></div>      
            </button>
            <div id=-4 style="display:none">
              <div class="grey-toggleBox">
                <a href="https://dl.acm.org/">all insights<img src="../assets/direct-download.png" class="downloadPNG"></a> <br>
                <a href="https://dl.acm.org/">only confirmed insights<img src="../assets/direct-download.png" class="downloadPNG"></a>
              </div>
            </div>
          </div>
        </div>
        <div class="grey-insight">
          <div class="grey-insight-name">
            add relevant insight
          </div>
          <div class="grey-insight-button">
            <button class="grey-button" @click="visible(-5)">
            <div id=-1005 style="display:inline"><img class="img-button" src="../assets/add.png" ></div>
            <div id=-2005 style="display:none"><img class="img-button" src="../assets/arrow-up.png" ></div>      
            </button>
            <div id=-5 style="display:none">
              <div class="grey-toggleBox">
                <input type="text" autocomplete="off" @keyup.enter='saveUserInput(), sendUserInsight()' @input = "filterParameters" v-model="userInput" class="grey-add-inputfield" @focus = "modal = true"/>
                <div v-if="filtered && modal">
                  <ul>
                    <li class = "autocomplete" v-for="param in filtered" :key ="param"  @click = "setParam(param)">
                      {{param}}
                    </li>
                  </ul>
                </div>
                <div class="submit-button2">
                  <button type="button" class="submit-button" @click='saveUserInput(), sendUserInsight()'>Save</button>
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
      autocomplete: [
        'Accuracy', 'Area' , 'F1', 'Recall', 'MSE', 'Precision', 'Classification Error'
      ],
      filtered: [],
      modal: false
    }
  },
  methods: {
    // Function only for testing
    toggle () {
      alert('Works!')
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
        this.$store.dispatch('loadMetadata')}
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
      this.$store.dispatch('loadMetadata')}
    },
  
    sendDownloadRequest() {
      this.$store.dispatch("loadDownload")
    },
    // DEPRECATED
    saveSelectedError(name){
      this.$store.dispatch('fetchError', name)
      alert('Thanks for reporting an error')
    },
    // User sends relevance of insight (upvote) on insight click
    sendInsightRelevance(){
      this.$store.dispatch('sendRateRelevanceInsight')
      this.$store.dispatch('loadMetadata')
    },

    sendInsightNotRelevantError() {
      this.$store.dispatch('sendInsightNotRelevantError')
      this.$store.dispatch('loadMetadata')
    },
    sendValueError() {
      this.$store.dispatch('sendValueError')
      this.$store.dispatch('loadMetadata')
    },
     sendTypeError() {
       this.$store.dispatch('sendTypeError')
        this.$store.dispatch('loadMetadata')
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
        'currentCategories'
    ]),

  }

}

</script>

<style scoped>

.extension {
  box-sizing: border-box;
  width: 300px;
  padding-bottom: 10px;
  background-color:#ffffff;
  font-family: Arial, Helvetica, sans-serif, sans-serif;
  font-size: 15px;
}

.main-column{
  display: block;
  padding-top: 20px;
  padding-left: 10px;
  padding-right: 10px;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 120%;
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
  text-align: center;
  padding: 8px;
  margin-top: 30px;
  margin-left: -384%;
  margin-right: -8px;
  margin-bottom: -8px;
  border-radius: 0px 0px 5px 5px;
  background-color: #FFFFFF;
  }

  .grey-button {
    border: none;
    background: white;
    width: 30px;
    height: 30px;
    float: right;
  }

  .grey-add-inputfield {
    width: 60%;
    padding-top: 8px;
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
    background-color: white;
    text-align: center;
    padding: 10px;
    margin-top: 30px;
    margin-left: -384%;
    margin-right: -8px;
    margin-bottom: -8px;
    border-radius: 0px 0px 5px 5px;
    box-shadow: 3px 3px 3px silver;
  }

  /*
  .insight-answers{
    
  }
  */

/* -button | design for buttons*/
  .submit-button {
    margin: 15px;
    border: none;
    color: rgb(235, 235, 235);
    background: rgb(20, 38, 176);
    border-radius: 5px;
    width: 70px;
    height: 30px;
  }

  .submit-button:hover { 
    color: black;
    background: rgb(184, 184, 184);}

  .submit-button2 {
    display:flex;
    justify-content: center;
    align-content: center;
    padding: 15px;
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
    height: 30px;
    width: 50px;
    margin: 5px;
    padding: 5px;
    background-color: rgb(225, 225, 92);
    border: 1px solid rgba(48, 48, 48, 0.94)
  }

  .answer-button:hover {
    background-color: lightgray;
    border: 1px solid rgba(48, 48, 48, 0.94);
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
    font-size: 50%;
    width: 35%;
    border: 1px solid rgba(48, 48, 48, 0.94);
    border-radius: 2px;
    margin-bottom: 10px;
    margin-top: -10px;
  }

  .error-button:hover { 
    color: black;
    background: rgb(184, 184, 184);
  }
  
  .error-button-2 {
    width: 90%;
    border: 1px solid rgba(48, 48, 48, 0.94);
    background-color: red;
    border-radius: 5px;
    margin-bottom: 10px;
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

.displayAnswer {
  font-weight: bold;
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
