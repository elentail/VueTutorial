<template>
  <div id="app">
    <b-container fluid class="bv-example-row">
      <div class="w-75 m-auto">
      <b-row>
        <b-col cols="6"><directive-example/></b-col>
        <b-col cols="6"><directive-example/></b-col>
      </b-row>   
      </div>
    </b-container> 
    <chart-example/>
    <!-- <component-example/> -->
    <HelloWorld/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
// import ComponentExample from "./components/ComponentExample.vue";
import DirectiveExample from "./components/DirectiveExample.vue";
import ChartExample from "./components/ChartExample.vue"

export default {
  name: 'App',
  components: {
    HelloWorld,
    // ComponentExample,
    DirectiveExample,
    ChartExample
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
