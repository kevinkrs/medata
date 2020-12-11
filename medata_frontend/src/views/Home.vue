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
        <!--The div element "box 2" represents one insight listed under the legend and also consists of
        a short text and a colored box. ... (V-for und v-bind:key kommentiere ich noch)-->
        <div class="box-2" v-for="entry in metadata" :key="entry.id">
          {{entry.name}}
          <!--Each insight can have either a green, yellow or red button.
          An v-if will create these buttons colored red, yellow or green
          depending on whether the passed numerical value "confirmed" inside the "metadaata" array
          (recieved inside script from the store file)is 0,1 or something else.-->
          <button v-if="entry.insight_upvotes < 1 " class="insight-button-red" @click="toggle"> </button> <!--Conditional einbauen, je nach id andere richtige-farbige Box einfügt-->
          <button v-else-if="entry.insight_upvotes < 8" class="insight-button-yellow" @click="toggle"> </button>
          <button v-else class="insight-button-green" @click="toggle"> </button>
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
    }
  },
  // mapstate is a Vuex component (using computed) summarizing the command of this.$store.state.metadata
  computed: mapState({
    metadata: state => state.metadata
  }),
  // This function starts the method "loadMetadata" belonging to "action" inside the store file
  // loadMetadata fetches the data from the api folder, which receives metadata from the backend
  // after metadata is reveived it is passed to the "mutation" component and after that to the "state" to save it
  beforeMount () {
    this.$store.dispatch('loadMetadata')
  }
}

</script>

<style scoped>

.extension {
  box-sizing: border-box;
  width: 300px;
  background-color: rgb(232, 232, 232);
  font-family: Arial, Helvetica, sans-serif;
  font-size: 15px;
}
legend {
  font-size: 15px, 
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

 .insight-button-green {
   border: none;
   background: green;
   width: 30px;
   height: 30px;
 }
  .insight-button-yellow {
   border: none;
   background: yellow;
   width: 30px;
   height: 30px;
 }
  .insight-button-red {
   border: none;
   background: red;
   width: 30px;
   height: 30px;
 }
  .insight-button:focus{
    width: 60px;
  }
.box-2{
  display: flex;
  justify-content: space-between;
  padding: 10px;
}
.box-3{
  padding: 15px;
  margin-top: 20px;
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
  background: rgb(206, 107, 20);
}

.downloadPNG {
  margin-right: 10px;
}
</style>
