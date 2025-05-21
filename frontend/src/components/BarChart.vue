<template>
  <Bar id="my-chart-id" :options="chartOptions" :data="computedChartData" />
</template>

<script>
import { computed } from "vue";
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

// 註冊 Chart.js 元件
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "BarChart",
  components: {
    Bar,
  },
  props: {
    labels: {
      type: Array,
      required: true,
      default: () => [],
    },
    granularity: {
      type: String,
      default: "month", // 'week' or 'month'
    },
    data: {
      type: Array,
      required: true,
      default: () => [],
    },
    title: {
      type: String,
      default: "Monthly Data Overview",
    },
  },
  setup(props) {
    // 計算屬性：動態生成 chartData
    const computedChartData = computed(() => ({
      labels: props.labels,
      datasets: [
        {
          label: `${props.granularity} Data`,
          data: props.data,
          backgroundColor: "skyblue",
        },
      ],
    }));

    // 圖表選項（包含動態表頭）
    const chartOptions = computed(() => ({
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: props.title,
          font: {
            size: 18,
          },
          color: "#333",
          padding: {
            top: 10,
            bottom: 10,
          },
          align: "center",
        },
        legend: {
          position: "top",
        },
      },
    }));

    return {
      computedChartData,
      chartOptions,
    };
  },
};
</script>
