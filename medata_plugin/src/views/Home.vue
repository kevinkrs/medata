/* eslint-disable indent */
<template>
<div class = "extension">
      <div class="main-column">
        <img class="logo" src="../assets/medata_black.png" width="200">
        <!--The fieldset element "box-1" contains everything reagardin the legend-->
        <fieldset class="box-1">
          <legend>Legend</legend>
          <!--The three div elements "box-1-content" represent the the three elements inside the legend.
          Each element consists of a short text and a colored box-->
          <div class="box-1-content">
            confirmed insigth
            <div class="colorboxgreen">
            </div>
          </div>
          <div class="box-1-content">
            validation needed
           <div class="colorboxyellow">
            </div>
          </div>
          <div class="box-1-content">
            enter information
            <div class="colorboxred">
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
        <div class="box-2" v-for="entry in metadata" :key="entry.id">
          <div class="box-2-name">
            {{entry.name}}
          </div>
          <!--Each insight can have either a green, yellow or red button and the corresponding toggle box.
          An v-if will create these buttons colored red, yellow or green and the corresponding toggle box
          depending on whether the passed numerical value "confirmed" inside the "metadaata" array
          (recieved inside script from the store file)is 0,1 or something else.-->
          
          <!--TODO insigth_upvores is not the right variable for comparision-->
          <div v-if='entry.answer.length == 0'>
            <!--With a click on the colored button the function visable is called and the id of the insight
            is passed. This ensures that the corresponding toggle box becomes visible.-->
            <button class="insight-button-red" @click="visible(entry.id)"></button>
            <div :id=entry.id style="display:none">
              <!--The div elements toggle-box-red/yellow/green define the frame of the three different
              toggle boxes-->
              <div class="toggle-box">
                <p>Please enter information:</p>
                <button style="width:80%">...</button><br>
                <button style="background-color:green">submit</button>
              </div>
            </div>
          </div>
          <!--TODO entry.answer[0].answer_score -> kills the frontend -->
          <div v-else-if="entry.answer.answer_score < 6">
            <button class="insight-button-yellow" @click="visible(entry.id)"> </button>
            <div :id=entry.id style="display:none">
              <div class="toggle-box">
                <!---->
                  <p>Please select <br> the correct Answer</p>
                  {{entry.answer}}
                  <button>other value</button>
              </div>
            </div>
          </div>

          <div v-else>
            <button class="insight-button-green" @click="visible(entry.id)"></button>
            <div :id=entry.id style="display:none">
              <div class="toggle-box">
                <!--If function, for checking if the answer has highest upvotes-->
                <p>{{entry.name}}: <br></p>
              <p>
                {{entry.insight_upvotes}} users confirmed <br>
                this information <br>
                </p>
                <button style="background-color:green">confirm</button>
                <button style="background-color:red">report an error</button>
              </div>
            </div>
          </div>
        </div>

        <div class="box-3">
        <a href="https://dl.acm.org/"><img src="@/assets/direct-download.png" class="downloadPNG"> download insights</a>
        </div>
        <div class="box-4">
          <p> Ad relevant parameters </p>
          <input type="text" v-model="userInput" class="inputfield"/>
          <p> {{userInput}} </p>
        </div>
        <div class="submit">
          <input type="button" value="Submit" class="submitbutton">
        </div>
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
      userInput: ''
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
        document.getElementById(divId).style.display = 'inline'
      } else {
        document.getElementById(divId).style.display = 'none'
      }
    },
    checkURL() {
      alert(this.query)
    },
    checkAnswers() {
      alert()
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
  padding-bottom: 70px;
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
}
.logo{
  margin-bottom: 15px;
}
.box-1{
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  border: 1px solid black;
  padding: 10px;
  margin-bottom: 20px;
}

legend {
  font-family: 'Courier New', Courier, monospace;
  margin-left: 5px;
}

 .box-1 .box-1-content{
   display: flex;
   padding-top: 20px;
   justify-content: space-between;
   margin: 3px;
 }

 .box-1 .colorboxgreen {
   box-sizing: border-box;
   background: green;
   width: 30px;
   height: 30px;
 }

 .box-1 .colorboxyellow {
   box-sizing: border-box;
   background: yellow;
   width: 30px;
   height: 30px;
 }

 .box-1 .colorboxred {
   box-sizing: border-box;
   background: red;
   width: 30px;
   height: 30px;
 }

.box-2{
  display: flex;
  justify-content: space-between;
  padding: 10px;
}

  .box-2-name {
    width: 50%;
    height: 30px;
    padding-top: 8px;
    text-align: left;
  }

  .box-2-button {
    width: 50%;
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
 }
  .insight-button:focus{
    width: 60px;
  }

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
  padding: 15px;
  display:flex;
  justify-content: center;
  align-content: center;
  
}

.submit .submitbutton{
  border: none;
  color: rgb(235, 235, 235);
  background: rgb(20, 38, 176);
  border-radius: 5px;
  width: 70px;
  height: 30px;
}

.submitbutton:hover{
  color: black;
  background: rgb(184, 184, 184);
}

.downloadPNG {
  margin-right: 10px;
}

.toggle-box {
  background-color: white;
  text-align: center;
  font-size: 130%;
  padding: 10px;
  margin-top: 30px;
  margin-left: -100%;
}

</style>
