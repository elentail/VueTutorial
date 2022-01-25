<template>
  <div id="app">
    <div class="container fluid">
      <div class="row">
        <div class="col-6"><code-viewer :content="tf_code" :title="'Tensorflow'" /></div>
        <div class="col-6"><code-viewer :content="torch_code" :title="'Pytorch'" /></div>
      </div>

    <hello-table />


      <div class="row m-5">
        <button type="button" class="btn btn-info btn-sm"  v-on:click="getStream">trainning</button>

        <chart-container ref="childComponentRef"/>
      </div>
      
    </div>
  </div>
</template>

<script>

import CodeViewer from "./components/CodeViewer.vue";
import ChartContainer from "./components/ChartContainer.vue"
import HelloTable from "./components/HelloTable.vue"

export default {
  name: 'App',
  components: {
    CodeViewer,
    ChartContainer,
    HelloTable
  },
  data(){
    return {
      tf_code: null,
      torch_code: null
    }
  },
  methods:{
    getStream : function(){
      this.$refs.childComponentRef.reload();
    }
  },
  mounted(){

    fetch("http://127.0.0.1:5000/codes")
      .then(response => response.json())
      .then(data => {
        this.tf_code =  data.tf_code;
        this.torch_code = data.torch_code;
      })
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
