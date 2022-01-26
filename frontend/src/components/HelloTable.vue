<template>
  <div ref="table"></div>
</template>
<script>

import {TabulatorFull as Tabulator} from 'tabulator-tables'; //import Tabulator library
// import 'tabulator-tables/dist/css/tabulator.min.css'
import 'tabulator-tables/dist/css/tabulator_site.min.css'

export default {
  name: "HelloTable",
  data: function () {
    return {
      tabulator: null, //variable to hold your table
      tableData: [
  {id:1, name:"Oli Bob", age:"12", col:"red", dob:""},
  {id:2, name:"Mary May", age:"1", col:"blue", dob:"14/05/1982"},
  {id:3, name:"Christine Lobowski", age:"42", col:"green", dob:"22/05/1982"},
  {id:4, name:"Brendon Philips", age:"125", col:"orange", dob:"01/08/1980"},
  {id:5, name:"Margret Marmajuke", age:"16", col:"yellow", dob:"31/01/1999"},
],
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
      layout:"fitColumns",
      pagination:"local",
    paginationSize:6,
    paginationSizeSelector:[3, 6, 8, 10],
    columns:[
  { title: "Name", field: "name", width: 150 },
  { title: "Age", field: "age", hozAlign: "left", formatter: "progress" },
  { title: "Favourite Color", field: "col" },
  { title: "Date Of Birth", field: "dob", hozAlign: "center" },
  { title: "Rating", field: "rating", hozAlign: "center", formatter: "star" },
  { title: "Passed?", field: "passed", hozAlign: "center", formatter: "tickCross" }
  ],
    });
  },
}
</script>
<style scoped>
</style>