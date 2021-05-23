<template>
  <Navbar></Navbar>
  <router-view/>
  <Audio_player></Audio_player>
</template>

<script>
import Navbar from '../src/components/nav.vue'
import Audio_player from '../src/components/audio_player'
export default {
  components:{
    Navbar,
    Audio_player
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c&display=swap');
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: rgb(211, 211, 211);
}
*{
  padding: 0;
  margin: 0;
  font-family: 'M PLUS Rounded 1c', sans-serif;
}
.main_container{
  width:90%;
  display: flex;
}
a{
  outline: none;
  text-decoration: none;
  color: rgb(211, 211, 211);
}
body{
  background: #1c1c1c;
}
</style>
