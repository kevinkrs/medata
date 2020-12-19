/* eslint-disable indent */
<template>
<div class = "extension">
      <div class="main-column">
        <img class="logo" src="../assets/medata_black.png" width="200">
        <!--The fieldset element "box-1" contains everything reagardin the legend-->
        <fieldset class="legend-frame">
          <legend>Legend</legend>
          <!--The three div elements "box-1-content" represent the the three elements inside the legend.
          Each element consists of a short text and a colored box-->
          <div class="legend-insight">
            <div class="legend-insight-name">
              confirmed insigth
            </div>
            <div class="legend-insight-button">
              <button class="insight-button-green" @click="visible(-1)">
                <div id=-1001 style="display:inline"><img class="arrow" src="../assets/info.png" ></div>
                <div id=-2001 style="display:none"><img class="arrow" src="../assets/arrow-up.png" ></div>      
              </button>
              <div id=-1 style="display:none">
                <div class="legend-toggleBox">
                  <p>Detailed explanation of a green insight</p>
                </div>
              </div>
            </div>
          </div>
          <div class="legend-insight">
            <div class="legend-insight-name">
              validation needed
            </div>
            <div class="legend-insight-button">
              <button class="insight-button-yellow" @click="visible(-2)">
                <div id=-1002 style="display:inline"><img class="arrow" src="../assets/info.png" ></div>
                <div id=-2002 style="display:none"><img class="arrow" src="../assets/arrow-up.png" ></div>      
              </button>
              <div id=-2 style="display:none">
                <div class="legend-toggleBox">
                  <p>Detailed explanation of a yellow insight </p>
                </div>
              </div>
            </div>
          </div>
          <div class="legend-insight">
            <div class="legend-insight-name">
              enter information
            </div>
            <div class="legend-insight-button">
              <button class="insight-button-red" @click="visible(-3)">
                <div id=-1003 style="display:inline"><img class="arrow" src="../assets/info.png" ></div>
                <div id=-2003 style="display:none"><img class="arrow" src="../assets/arrow-up.png" ></div>      
              </button>
              <div id=-3 style="display:none">
                <div class="legend-toggleBox">
                  <p>Detailed explanation of a red insight </p>
                </div>
              </div>
            </div>
          </div>
        </fieldset>
      <div>
        <button @click="checkURL"> Check URL </button>
      </div>
      <div>
        <button @click="checkAnswers" >Check answers</button>
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
            <button class="insight-button-red" @click="visible(entry.id)">
              <div :id=entry.id-1000 style="display:inline"><img class="arrow" src="../assets/arrow-down.png" ></div>
              <div :id=entry.id-2000 style="display:none"><img class="arrow" src="../assets/arrow-up.png" ></div>      
            </button>
            <div :id=entry.id style="display:none">
              <!--The div elements toggle-box-red/yellow/green define the frame of the three different
              toggle boxes-->
              <div class="insight-toggleBox">
                <p>Please enter information:</p>
                  <!--TODO: implement button styles in CSS file-->
                <input placeholder="your relevant data"><br>
                <button class="submit-insight">submit</button>
              </div>
            </div>
          </div>
          <div div v-else-if="entry.answer[0].answer_score < 3" class="insight-button">
            <button class="insight-button-yellow" @click="visible(entry.id)">
              <div :id=entry.id-1000 style="display:inline"><img class="arrow" src="../assets/arrow-down.png" ></div>
              <div :id=entry.id-2000 style="display:none"><img class="arrow" src="../assets/arrow-up.png" ></div>
            </button>
            <div :id=entry.id style="display:none">
              <div class="insight-toggleBox">
                <div class="answers">
                  <p>Please select <br> the correct Answer</p>
                  <div class="row">
                    <div v-for="(index) in 4" :key ="index">
                      <button class="answerButton">{{entry.answer[index-1].answer}}</button>
                     <!-- TODO: When user clicks on one answer, it gets submitted and all the other answer switch to label (not interactable)
                      <label class="answerButton">{{entry.answer[index-1].answer}} </label>
                      -->
                    </div>
                  </div>
                </div>
                <!-- Code works, in worst case we take this one 
                <div class="answers">
                  <p>Please select <br> the correct Answer</p>
                  <div class="row1">
                    <button class="answerButton">{{entry.answer[0].answer}}</button>
                    <button class="answerButton">{{entry.answer[1].answer}}</button>
                  </div>
                  <div class="row2">
                    <button class="answerButton">{{entry.answer[2].answer}}</button>
                    <button class="answerButton">{{entry.answer[3].answer}}</button>
                </div>
                -->
                <br>
                <p> Add value </p>
                  <input class="userInput" v-model="userInput"> 
                  <button class="submit-insight" @click="submitUserInput">Submit</button>
              </div>
            </div>
          </div>
          <div v-else class="insight-button">
            <button class="insight-button-green" @click="visible(entry.id)">
              <div :id=entry.id-1000 style="display:inline"><img class="arrow" src="../assets/arrow-down.png" ></div>
              <div :id=entry.id-2000 style="display:none"><img class="arrow" src="../assets/arrow-up.png" ></div>
            </button>
            <div :id=entry.id style="display:none">
              <div class="insight-toggleBox">
                <!--If function, for checking if the answer has highest upvotes-->
                <p>{{entry.name}}: <br></p>
              <p>
                {{entry.insight_upvotes}} users confirmed <br>
                this information <br>
                </p>
                <button class="submit-insight">confirm</button>
                <button class="report-insight" >report an error</button>
              </div>
            </div>
          </div>
        </div>

        <div><br><br></div>


        <fieldset class="legend-frame">
          <legend>More functions</legend>
          <!--The three div elements "box-1-content" represent the the three elements inside the legend.
          Each element consists of a short text and a colored box-->
          <div class="legend-insight">
            <div class="legend-insight-name">
              download insights
            </div>
            <div class="legend-insight-button">
              <button class="function-button" @click="visible(-4)">
                <div id=-1004 style="display:inline"><img class="arrow" src="../assets/direct-download.png" ></div>
                <div id=-2004 style="display:none"><img class="arrow" src="../assets/arrow-up.png" ></div>      
              </button>
              <div id=-4 style="display:none">
                <div class="legend-toggleBox">
                  <a href="https://dl.acm.org/">all insights<img src="../assets/direct-download.png" class="downloadPNG"></a> <br>
                  <a href="https://dl.acm.org/">only confirmed insights<img src="../assets/direct-download.png" class="downloadPNG"></a>
                </div>
              </div>
            </div>
          </div>
          <div class="legend-insight">
            <div class="legend-insight-name">
              add relevant insight
            </div>
            <div class="legend-insight-button">
              <button class="function-button" @click="visible(-5)">
                <div id=-1005 style="display:inline"><img class="arrow" src="../assets/add.png" ></div>
                <div id=-2005 style="display:none"><img class="arrow" src="../assets/arrow-up.png" ></div>      
              </button>
              <div id=-5 style="display:none">
                <div class="legend-toggleBox">
                  <input type="text" v-model="userInput" class="function-inputfield"/>
                  <p> {{userInput}} </p>
                 <div class="submit">
                    <input type="button" value="Submit" class="submit-button">
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
      } else {
        document.getElementById(divId).style.display = 'none';
        document.getElementById(divId-1000).style.display = 'inline';
        document.getElementById(divId-2000).style.display = 'none';
      }
    },
    checkURL() {
      alert(this.query)
    },
    checkAnswers() {
      alert(this.metadata.answer)
    }
  },
  // mapstate is a Vuex component (using computed) summarizing the command of this.$store.state.metadata
  computed: 
    mapState([
      'metadata',
      'answer',
      'query',
    ]),

  // This function starts the method "loadMetadata" belonging to "action" inside the store file
  // loadMetadata fetches the data from the api folder, which receives metadata from the backend
  // after metadata is reveived it is passed to the "mutation" component and after that to the "state" to save it
  /*beforeMount () {
    this.$store.dispatch('loadMetadata')
  }*/
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
legend {
  font-size: 15px, 
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

/*Legend*/
  .legend-frame {
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
  }

 .legend-insight {
    display: flex;
    justify-content: space-between;
    padding-top: 5px;
    padding-bottom: 5px;
 }

  .legend-insight-name {
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

  .legend-insight-button {
    width: 20%;
    padding: 8px;
    background-color: rgb(232, 232, 232);
    box-shadow: 3px 3px 3px silver;
    border-radius: 0px 5px 5px 0px;
    border: 1px solid black;
    border-left-style: none;
  }

  .legend-toggleBox {
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

/*Insight List*/
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

/*More Fonctions*/
  .function-button {
    border: none;
    background: white;
    width: 30px;
    height: 30px;
    float: right;
  }

  .function-inputfield {
    width: 60%;
    padding-top: 8px;
  }


.submit-insight {
  margin: 15px;
  border: none;
  color: rgb(235, 235, 235);
  background: rgb(20, 38, 176);
  border-radius: 5px;
  width: 70px;
  height: 30px;
}

.submit-insight:hover { 
  color: black;
  background: rgb(184, 184, 184);}

.report-insight {
  margin: 15px;
  border: none;
  color: rgb(235, 235, 235);
  background: rgb(186, 15, 15);
  border-radius: 5px;
  width: 70px;
  height: 30px;
}

.report-insight:hover { 
  color: black;
  background: rgb(184, 184, 184);}

.box-3{
  padding: 15px;
  margin-top: 30px;
  text-align: center;
}

.box-4{
  display: block;
  margin-top: 20px;
  text-align: center;
}


.submit {
  display:flex;
  justify-content: center;
  align-content: center;
  padding: 15px;
  
}

.submit .submit-button{
  margin: 15px;
  border: none;
  color: rgb(235, 235, 235);
  background: rgb(20, 38, 176);
  border-radius: 5px;
  width: 70px;
  height: 30px;
}

.submit-button:hover{
  color: black;
  background: rgb(184, 184, 184);
}

.downloadPNG {
  width: 10%;
  margin-bottom: -5px;
}

.answerButton {
  height: 30px;
  width: 50px;
  margin: 5px;
  padding: 5px;
  background-color: rgb(225, 225, 92);
  border: 1px solid rgba(48, 48, 48, 0.94)
}
.answer{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.answerButton:hover {
  background-color: lightgray;
  border: 1px solid rgba(48, 48, 48, 0.94)
}

.arrow {
 width: 90%;
 margin-top: 22%;
}
</style>
