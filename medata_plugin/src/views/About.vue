<template>
<div class="container">
  <img src="../assets/medata_black.png" width="200">
  <div class="about">
      <h1>Welcome to Medata!</h1>
      <router-link to = "/home">  <button class ="mainButton">Start</button></router-link>
    </div>
  </div>
</template>


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
  width: 70px;
  height: 30px;
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