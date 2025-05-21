<!-- src/components/DataTable.vue -->
<template>
  <v-data-table
    :headers="resolvedHeaders"
    :items="items"
    :search="search"
    class="elevation-1 text-center"
  >
    <!-- 自己畫 header -->
    <template v-slot:headers>
      <tr>
        <th v-for="header in resolvedHeaders" :key="header.value" class="custom-header text-center">
          {{ header.text }}
        </th>
      </tr>
    </template>

    <!-- 自己畫每一行 -->
    <template v-slot:item="{ item }">
      <tr>
        <td>{{ item.employeeId }}</td>
        <td>{{ item.name }}</td>
        <template v-for="header in dynamicHeaders" :key="header.value">
          <td>
            <StatusCard :content="item[header.value]" @click="() => openDetail(item, header.value)"/>
          </td>
        </template>
      </tr>
    </template>
  </v-data-table>
  <v-dialog
      v-model="showDetail"
      persistent
      width="400"
      >
      <v-card>
          <v-card-title>
          Attendance Detail
          </v-card-title>

          <v-card-text>
          <div><strong>Date:</strong> {{ detailData.date }}</div>
          <div><strong>Employee ID:</strong> {{ detailData.employeeId }}</div>
          <div><strong>Name:</strong> {{ detailData.name }}</div>
          <div><strong>Attendance Status:</strong> {{ detailData.status }}</div>
          <div><strong>Clock-in Time:</strong> {{ detailData.clockInTime }}</div>
          <div><strong>Clock-in Gate:</strong> {{ detailData.clockInGate }}</div>
          <div><strong>Clock-out Time:</strong> {{ detailData.clockOutTime }}</div>
          <div><strong>Clock-out Gate:</strong> {{ detailData.clockOutGate }}</div>
          <div><strong>Duration:</strong> {{ detailData.duration }}</div>
          </v-card-text>

          <v-card-actions>
          <v-btn color="primary" block @click="showDetail = false">Close</v-btn>
          </v-card-actions>
      </v-card>
  </v-dialog>
</template>

<script>
import { ref, toRaw } from "vue";
import StatusCard from "./StatusCard.vue";

export default {
  name: "StatusTable",
  components: {
    StatusCard,
  },
  props: {
    headers: { type: Array, required: true },
    items: {
      type: Array,
      required: true,
    },
    search: {
      type: String,
      default: "",
    },
  },
  setup() {
    const showDetail = ref(false);  // 控制 dialog 開關
    const detailData = ref({
      date: '',
      employeeId: '',
      name: '',
      status: '',
      clockInTime: '',
      clockInGate: '',
      clockOutTime: '',
      clockOutGate: '',
      duration: '',
    });

    // 這個是點擊 StatusCard 時要呼叫的
    function openDetail(item, dateKey) {
      detailData.value = {
        date: dateKey,
        employeeId: item.employeeId,
        name: item.name,
        status: item[dateKey],
        clockInTime: '08:25:33',  // 先給假資料
        clockInGate: 'Main Gate',
        clockOutTime: '17:02:55',
        clockOutGate: 'Gate 11',
        duration: '8 hr(s) 38 min(s)',
      };
      showDetail.value = true; // 打開Dialog
    }

    return {
      showDetail,
      detailData,
      openDetail,
    };
  },
  computed: {
    resolvedHeaders() {
      const finalHeaders = Array.isArray(this.headers) ? this.headers : this.headers.value;
      return toRaw(finalHeaders);
    },
    dynamicHeaders() {
      return this.resolvedHeaders.filter(
        (header) =>
          header.value !== "employeeId" &&
          header.value !== "name"
      );
    },
  },
};
</script>

<style scoped>
.custom-header {
  background-color: #f5f5f5;
  color: black;
  font-weight: bold;
  text-align: center;
}
</style>
