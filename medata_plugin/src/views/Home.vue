
<template>
<div class = "extension">
  <div class="main-column">

    <!--Picture of the MEDATA logo-->
    <img class="logo" src="../assets/medata_black.png" width="200">

    <!--This fieldset element "grey-box" contains everything reagardin the legend-->
    <fieldset class="grey-box">
      <legend>Legend</legend>
      <!--The three div elements "grey-insight" represent the the three boxes/insights inside the legend-->
      <div class="grey-insight">
        <div class="grey-insight-name">confirmed insigth</div>
        <!--The div "grey-insight-button" contains the green/yellow or red button and the corresponding fold-out toggle box-->
        <div class="grey-insight-button">
          <button class="insight-button-green" @click="visible(-1)">
            <div id=-1001 style="display:inline"><img class="img-button" src="../assets/info.png" ></div>
            <div id=-2001 style="display:none"><img class="img-button" src="../assets/arrow-up.png" ></div>      
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
            <div id=-1002 style="display:inline"><img class="img-button" src="../assets/info.png" ></div>
            <div id=-2002 style="display:none"><img class="img-button" src="../assets/arrow-up.png" ></div>      
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
          <div id=-1003 style="display:inline"><img class="img-button" src="../assets/info.png" ></div>
          <div id=-2003 style="display:none"><img class="img-button" src="../assets/arrow-up.png" ></div>      
          </button>
          <div id=-3 style="display:none">
            <div class="grey-toggleBox">
              <p>Detailed explanation of a red insight </p>
            </div>
          </div>
        </div>
      </div>
    </fieldset>

    <div>
      <button @click="checkURL"> Check URL </button>
    </div>
    
    <!--If backend has no information to given category it's responding with an empty list. Here we check if the list is truly empty.
    If it is, we display first the first div class "noData". If not empty we display second div -->
    <div v-if='metadata.length == 0'>
      <div class="noData">
        <p> No data to this category available yet</p>
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
          <button class="insight-button-red" @click="visible(entry.id), saveInName(entry.name)">
            <div :id=entry.id-1000 style="display:inline"><img class="img-button" src="../assets/arrow-down.png" ></div>
            <div :id=entry.id-2000 style="display:none"><img class="img-button" src="../assets/arrow-up.png" ></div>      
          </button>

            <div :id=entry.id+1000 style="display:none">
              <div class="insight-toggleBox">
                <button class="error-button" @click="visible2(entry.id+1000)">back</button>
                <button class="error-button-2">Incorrect spelling/duplication</button> <br> 
                <button class="error-button-2">Not needed for this paper</button>
              </div>
            </div> 

          <div :id=entry.id style="display:none">
            <!--The div elements toggle-box-red/yellow/green define the frame of the three different
            toggle boxes-->
            <div class="insight-toggleBox">
              <button class="error-button" @click="visible2(entry.id+1000)">report an error</button>
              <p>Please enter information:</p>
                <!--TODO: implement button styles in CSS file-->
              <input placeholder="your relevant data" v-model='userInput'><br>
              <button class="submit-insight" @click="saveUserInput(), sendUserAnswer()">Submit</button>
            </div>
          </div>

        </div>
        <div div v-else-if="entry.answer[0].answer_score < 3" class="insight-button">
          <button class="insight-button-yellow" @click="visible(entry.id), saveInName(entry.name)">
            <div :id=entry.id-1000 style="display:inline"><img class="img-button" src="../assets/arrow-down.png" ></div>
            <div :id=entry.id-2000 style="display:none"><img class="img-button" src="../assets/arrow-up.png" ></div>
          </button>

            <div :id=entry.id+1000 style="display:none">
              <div class="insight-toggleBox">
                <button class="error-button" @click="visible2(entry.id+1000)">back</button>
                <button class="error-button-2">Incorrect spelling/duplication</button> <br> 
                <button class="error-button-2">Not needed for this paper</button>
              </div>
            </div> 

          <div :id=entry.id style="display:none">
            <div class="insight-toggleBox">
            <button class="error-button" @click="visible2(entry.id+1000)">report an error</button>
              <div class="insight-answers">
                <p>Please select <br> the correct Answer</p>
               <div class="row">
                    <div v-for="answer in entry.answer" :key ="answer">
                      <!--How can i connect v-model directly -->
                      <button type="button"  class="answer-button" @click="saveAnswerSelection(answer.answer), sendUpvote()">
                        {{answer.answer}}
                      </button>
                    </div>
                  </div>
              </div>
              <!-- Code works, in worst case we take this one 
              <div class="insight-answers">
                <p>Please select <br> the correct Answer</p>
                <div class="row1">
                  <button class="answer-button">{{entry.answer[0].answer}}</button>
                  <button class="answer-button">{{entry.answer[1].answer}}</button>
                </div>
                <div class="row2">
                  <button class="answer-button">{{entry.answer[2].answer}}</button>
                  <button class="answer-button">{{entry.answer[3].answer}}</button>
              </div>
              -->
              <br>
              <p> Add value </p>
                <input class="userInput" v-model="userInput"> 
                <button class="submit-insight" @click=" saveUserInput(), sendUserAnswer()">Submit</button>
            </div>
          </div>
        </div>
        <div v-else class="insight-button">
          <button class="insight-button-green" @click="visible(entry.id), saveInName(entry.name)">
            <div :id=entry.id-1000 style="display:inline"><img class="img-button" src="../assets/arrow-down.png" ></div>
            <div :id=entry.id-2000 style="display:none"><img class="img-button" src="../assets/arrow-up.png" ></div>
          </button>

            <div :id=entry.id+1000 style="display:none">
              <div class="insight-toggleBox">
                <button class="error-button" @click="visible2(entry.id+1000)">back</button>
                <button class="error-button-2">Incorrect spelling/duplication</button> <br> 
                <button class="error-button-2">Not needed for this paper</button>
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
              <button class="submit-button" @click='sendUpvote()'>confirm</button>
              <button class="report-button" >report an error</button>
            </div>
          </div>
        </div>
      </div>

      <div><br><br></div>

      <!--This fieldset element "grey-box" contains everything reagardin the "more-functions"-->
      <fieldset class="grey-box">
        <legend>more functions</legend>
        <!--The three div elements "box-1-content" represent the the three elements inside the legend.
        Each element consists of a short text and a colored box-->
        <div class="grey-insight">
          <div class="grey-insight-name">
            download insights
          </div>
          <div class="grey-insight-button">
            <button class="grey-button" @click="visible(-4)">
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
                <input type="text" v-model="userInput" class="grey-add-inputfield"/>
                <p> {{userInput}} </p>
                <div class="submit-button2">
                  <input type="button" value="submit" class="submit-button">
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
     // currentInName: '',
     // selectedAnswer: '',
    }
  },
  methods: {
    // Function only for testing
    toggle () {
      alert('Works!')
    },
    // TODO commments
    visible: function (divId) {
      if (document.getElementById(divId).style.display === 'none') {
        document.getElementById(divId).style.display = 'inline';
        document.getElementById(divId-1000).style.display = 'none';
        document.getElementById(divId-2000).style.display = 'inline';
        document.getElementById(divId+1000).style.display = 'none';
      } else {
        document.getElementById(divId).style.display = 'none';
        document.getElementById(divId-1000).style.display = 'inline';
        document.getElementById(divId-2000).style.display = 'none';
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
    saveUserInput() {
      this.$store.dispatch('fetchUserInput', this.userInput)
    },

    // This methods dispatch functions that are sending given user interaction to the backend 
    sendUserAnswer() {
      //This method sends the answer (yellow-status, red-status) the user has written into the input field
      this.$store.dispatch('sendAnswer')
      alert('Thanks for submitting!')
      this.userInput = ''
    },
    sendUpvote() {
      // This method sends the answer (yellow-status, green-status) the user has selected as the right one, or in the green-status case just confirming it as true once more
      this.$store.dispatch("sendRateAnswer")
      alert('Thanks vor submitting!')
    }
  },
  // mapstate is a Vuex component (using computed) summarizing the command of this.$store.state.metadata
  // we can easily load all our state objects inside our Home-Component and access it by calling this."propertyname"
  computed: {
    ...mapState([
        'metadata', 
        'currentIn',
        'currentAnswer',
        'currentUserInput'
    ]),

  }

}

</script>

<style scoped>

.extension {
  box-sizing: border-box;
  width: 300px;
  padding-bottom: 10px;
  background-color: rgb(232, 232, 232);
  font-family: Arial, Helvetica, sans-serif;
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

.logo{
  margin-bottom: 15px;
}

/*grey- | design for "Legend" and "more functions"*/
 .grey-box {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    border: 1px solid black;
    padding: 10px;
    margin-bottom: 20px;
    box-shadow: 3px 3px 3px silver;
  }
  
  legend {
    margin-left: 5px;
    font-size: 15px, 
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
    background-color:  rgb(232, 232, 232);
    box-shadow: 3px 3px 3px silver;
    border-radius: 5px 0px 0px 5px;
    border: 1px solid black;
    border-right-style: none;
  }

  .grey-insight-button {
    width: 20%;
    padding: 8px;
    background-color: rgb(232, 232, 232);
    box-shadow: 3px 3px 3px silver;
    border-radius: 0px 5px 5px 0px;
    border: 1px solid black;
    border-left-style: none;
  }

  .grey-toggleBox {
  text-align: center;
  padding: 8px;
  margin-top: 30px;
  margin-left: -382%;
  margin-right: -9px;
  margin-bottom: -8px;
  border-radius: 0px 0px 5px 5px;
  background-color:rgb(232, 232, 232);
  box-shadow: 3px 3px 3px silver;
  border: 1px solid black;
  border-top-style: none;
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
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 5px;
    padding-bottom: 5px;
  }

  .insight-name {
    width: 80%;
    height: 30px;
    padding: 8px;
    text-align: left;
    background-color: white;
    box-shadow: 3px 3px 3px silver;
    border-radius: 5px 0px 0px 5px;
  }

  .insight-button {
    width: 20%;
    padding: 8px;
    background-color: white;
    box-shadow: 3px 3px 3px silver;
    border-radius: 0px 5px 5px 0px;
  }

 .insight-button-green {
   border: none;
   background: green;
   width: 30px;
   height: 30px;
   float: right;
   }

  .insight-button-yellow {
   border: none;
   background: yellow;
   width: 30px;
   height: 30px;
   float: right;
 }
  .insight-button-red {
   border: none;
   background: red;
   width: 30px;
   height: 30px;
   float: right;
   font-weight: bold;
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
    border: 1px solid rgba(48, 48, 48, 0.94)
  }

  .img-button {
    width: 90%;
    margin-top: 22%;
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


</style>
