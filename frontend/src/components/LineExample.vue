<template>
    <LineChart :chart-data="linechartdate" :options="options" />

</template>


<script>
import LineChart from './LineChart.vue';

export default {
  name: 'LineExample',
  components: {
    LineChart
  },
  data() {
    return {
      serverMessage: {},
      messageCount: 0,
      activeChatRooms: 0,
      recentLogins: [],
      openTickets: 0,
      closedTickets: 0,
      unassignedTickets: 0,
      linechartdate:{
        datasets: [
            {
                label: 'Loss',
                data: [12, 19, 3, 5, 2, 3],
                borderWidth: 1
            }
        ]
        }
    };
  },
  computed: {

    options() {
      return {
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
      };
    },
  },
  mounted() {
    // add an event listener to metrics created event
    this.establishConnection();
  },
  methods: {
    establishConnection() {
    },
  },
};
</script>
