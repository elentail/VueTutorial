<template>
    <BarChart :chart-data="barchartdata" :options="options" />

</template>


<script>
import BarChart from './BarChart.vue';

export default {
  name: 'BarExample',
  components: {
    BarChart,
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
    };
  },
  computed: {

    barchartdata() {
      return {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [
            {
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }
        ]
        }
    },
    
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
