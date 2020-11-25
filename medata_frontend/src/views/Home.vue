<template>
  <div id="home">
    <main>
      <div class="header">
        <router-link to ="/"><img src="../assets/medata-white.png" width="300"></router-link>
        <br>
           <a href="mailto:support@medata.com" target="_blank">
         <img class="mail" src="../assets/email.png">
        </a>
        <a href="https://github.com/kevinkrs7/medata" target="_blank">
         <img class="github" src="../assets/github.png">
        </a>
      </div>
      <div class="search-box">
        <input type="text" class="search-bar" placeholder="https://dl.acm.org/..."
        v-model="query" @keypress.enter="openSearch"/>

        <input type="submit" class="button" id="srch" value="Find" @click="openSearch()" target="self">
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      substr: 'https://dl.acm.org/',
      query: ''
    }
  },
  methods: {
    openSearch () {
    // eslint-disable-next-line no-var
      var querySub = this.query.substring(0, 19)
      if (querySub === this.substr) {
        window.open(this.query, '/embed')
      } else {
        alert('Please paste valid URL')
      }
    }
  }
}

</script>

<style> /* "Scoped" restricts css localy on this view */

main {
  min-height: 100vh;
  padding: 25px;
  margin:0px;
  background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.75));
  background-image: url('../assets/IMG_1484.jpg');
  background-size: cover;
  background-position: bottom;
  font-family: 'Futura', sans-serif;
}
.search-box {
  width: 30%;
  margin-top: 30px;
  margin-bottom: 30px;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}

.search-box .button {
  width: 50%;
  background-color: rgb(148, 148, 148);
  border-radius: 15px;
  outline: none;
  appearance: none;
  border: none;
  padding: 5px;
}
.search-box .button:hover{
  background-color: rgb(42, 75, 160);
  border-radius: 15px;
  color: white;
  outline: none;
  appearance: none;
  border: none;
}

.search-box .search-bar {
  display: block;
  width: 100%;
  padding: 15px;
  margin-bottom: 5px;
  color: #313131;
  font-size: 20px;
  appearance: none;
  border:none;
  outline: none;
  background: none;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 0px 16px 0px 16px;
  transition: 0.4s;
}
.search-box .search-bar:focus {
  box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 0.75);
  border-radius: 16px 0px 16px 0px;
}

.header {
  display: block;
  text-align: right;
  margin-bottom: 200px;
}

.header .github{
  margin-left: 10px;
}

</style>
