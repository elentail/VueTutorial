<template>
  <div id="app">
    <div class="container fluid">
      <div class="row">
        <div class="col-6"><directive-example/></div>
        <div class="col-6"><directive-example/></div>
      </div>
      <div class="row">
          <button type="button" class="btn btn-success btn-sm"  v-on:click="getStream">trainning</button>
      </div>

      <div class="row">
        <div class="col-6"><line-example ref="linechart"/></div>
        <div class="col-6"><bar-example/></div>
      </div>
    </div>
    <!-- <component-example/> -->
    <!-- <HelloWorld/> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import ComponentExample from "./components/ComponentExample.vue";
import DirectiveExample from "./components/DirectiveExample.vue";
// import ChartExample from "./components/ChartExample.vue"
import LineExample from "./components/LineExample.vue"
import BarExample from './components/BarExample.vue';
// import axios from 'axios';

export default {
  name: 'App',
  components: {
    // HelloWorld,
    // ComponentExample,
    DirectiveExample,
    // ChartExample,
    LineExample,
    BarExample
  },

  methods:{
    getStream : function(){

      // var path = "http://localhost:5000/api/stream"
      // axios.get(path).then((res) => {
      //   console.log(res);
      // }).catch((error) => {
      //   console.error(error);
      // });
      if (typeof (EventSource) !== "undefined") {
        var eventSource = new EventSource(
          "http://localhost:5000/api/stream");

        eventSource.addEventListener('open', function () {
          console.log("Opened connection to event stream!");
        }, false);

        eventSource.addEventListener('error', function () {
          console.log("Errored!");
        }, false);

        eventSource.addEventListener('message', function (e) {
          //var parsedData = JSON.parse(e.data);
          //let cat = parseInt(parsedData.data)
          console.log(e.data)
          // console.log(this.$root.$refs.linechart)
        }, false);    

        eventSource.addEventListener('error', function(e) {
          if (e.readyState == EventSource.CLOSED) {
            // Connection was closed.
          }
          eventSource.close();

        }, false);


      }

    }
  },
  mounted(){
    console.log(this.$refs.linechart.linechartdate.datasets[0].data)
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
