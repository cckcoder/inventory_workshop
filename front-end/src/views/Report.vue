<template>
    <div class="container mt-4">
        <div class="column is-9">
          <vue3-chart-js v-bind="{ ...pieChart }" />
        </div>
    </div>
</template>

<script>
import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'

export default {
  name: 'Report',
  components: {
    Vue3ChartJs
  },
  setup() {
    const pieChart = {
      type: "pie",
      data: {
        labels: ["VueJs", "EmberJs", "ReactJs", "AngularJs"],
        datasets: [
          {
            backgroundColor: ["#41B883", "#E46651", "#00D8FF", "#DD1B16"],
            data: [40, 20, 80, 10],
          },
        ],
      },
    }

    return {
      pieChart,
    };
  }
}
</script>
