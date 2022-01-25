<template>
  <div ref="table"></div>
</template>
<script>

import {TabulatorFull as Tabulator} from 'tabulator-tables'; //import Tabulator library
import 'tabulator-tables/dist/css/tabulator.min.css'

export default {
  name: "HelloTable",
  data: function () {
    return {
      tabulator: null, //variable to hold your table
      tableData: [ ]
    }
  },
  watch:{
    //update table if data changes
    tableData:{
      handler: function (newData) {
        this.tabulator.replaceData(newData);
      },
      deep: true,
    }
  },
  mounted(){
    //instantiate Tabulator when element is mounted
    this.tabulator = new Tabulator(this.$refs.table, {
      data: this.tableData, //link data to table
      reactiveData:true, //enable data reactivity,
    columns:[
    {title:"Name", field:"name"},
    {title:"Progress", field:"progress", hozAlign:"right", sorter:"number"},
    {title:"Gender", field:"gender"},
    {title:"Rating", field:"rating", hozAlign:"center"},
    {title:"Favourite Color", field:"col"},
    {title:"Date Of Birth", field:"dob", hozAlign:"center", sorter:"date"},
    {title:"Driver", field:"car", hozAlign:"center"},
    ],
    });
  },
}
</script>
<style scoped>
</style>