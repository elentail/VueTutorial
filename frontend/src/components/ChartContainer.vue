<template>
  <div class="container">
    <line-chart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import LineChart from './Chart.vue'

export default {
  name: 'LineChartContainer',
  components: { LineChart },
  data: () => ({
    loaded: false,
    chartdata: null,
    options:{
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false,
        },
        scales: {
            xAxes: [{
                barPercentage: 0.5,
                gridLines: {
                    display: true
                }
            }],
            y: {
                beginAtZero: true
            },
            yAxes: [{
                gridLines: {
                    display: false
                }   
            }]            
        },
    }
  }),
  mounted () {
    this.loaded = false
    fetch("http://localhost:5000/api/chart")
      .then(response => response.json())
      .then(data => {
          this.chartdata = data
          this.loaded = true
      })
  },
  methods:{
    reload: function(){
    this.loaded = false
    fetch("http://localhost:5000/api/chart2")
      .then(response => response.json())
      .then(data => {
          this.chartdata = data
          this.loaded = true
      })
    }
  }

}
</script>