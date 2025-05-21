<template>
  <v-app>
    <SideBar>
      <v-container>
        <v-row
          ><v-col><h2>Department</h2></v-col></v-row
        >
        <v-row>
          <v-col>
            <v-card flat width="30%">
              <SelectBox
                v-model="selectedDepartment"
                :items="Department"
              ></SelectBox>
            </v-card>
          </v-col>
        </v-row>
        <!-- 放總體出勤分析表 -->
        <v-row>
          <v-col><h2>Over Time Summary</h2></v-col>
          <v-col cols="auto">
            <v-btn variant="tonal" color="blue"> This Month </v-btn>
          </v-col>
          <v-col cols="auto">
            <v-btn variant="tonal" color="blue"> This Week </v-btn>
          </v-col>
        </v-row>
        <v-row class="mb-6">
          <v-col>
            <v-card>
              <v-table class="d-flex justify-center">
                <thead>
                  <tr>
                    <th
                      v-for="header in headers"
                      :key="header.value"
                      class="text-center"
                      style="background-color: #f5f5f5"
                    >
                      {{ header.text }}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="item in summary"
                    :key="item.name"
                    class="text-center"
                  >
                    <td>
                      <WorkSummaryCard
                        :totalWorkHours="item.TotalWorkHours"
                        :unit="'hr'"
                        :timeUnit="'month'"
                        :lastRecord="1968"
                      />
                    </td>
                    <td>
                      <WorkSummaryCard
                        :totalWorkHours="item.TotalOTHours"
                        :unit="'hr'"
                        :timeUnit="'month'"
                        :lastRecord="1968"
                      />
                    </td>
                    <td>
                      <WorkSummaryCard
                        :totalWorkHours="item.OTHoursPerson"
                        :unit="'hr'"
                        :timeUnit="'month'"
                        :lastRecord="12.3"
                      />
                    </td>
                    <td>
                      <WorkSummaryCard
                        :totalWorkHours="item.OTHeadcounts"
                        :unit="'p'"
                        :timeUnit="'month'"
                        :lastRecord="9"
                      />
                    </td>
                  </tr>
                </tbody>
              </v-table>
            </v-card>
          </v-col>
        </v-row>
        <!-- 長條圖 -->
        <v-row>
          <v-col><h2>Analysis Chart</h2></v-col>
        </v-row>
        <v-row align="center">
          <v-col cols="auto">
            <v-card elevation="0" class="datepicker-container">
              <VueDatePicker
                v-model="Startdate"
                class="custom-datepicker"
                teleport="body"
                ref="startDatePicker"
                type="date"
                :enable-time-picker="false"
              />
            </v-card>
          </v-col>
          <v-col cols="auto">to</v-col>
          <v-col cols="auto">
            <v-card elevation="0" class="datepicker-container">
              <VueDatePicker
                v-model="Enddate"
                class="custom-datepicker"
                teleport="body"
                ref="endDatePicker"
                :enable-time-picker="false"
              />
            </v-card>
          </v-col>
          <v-col cols="auto" class="d-flex align-center">
            <v-radio-group
              inline
              class="d-flex align-center"
              v-model="granularity"
            >
              <v-radio label="Day" value="day"></v-radio>
              <v-radio label="Week" value="week"></v-radio>
              <v-radio label="Month " value="month"></v-radio>
            </v-radio-group>
          </v-col>
        </v-row>
        <v-row class="mb-6">
          <bar-chart
            :data="data"
            :granularity="granularity"
            :labels="LabelData"
            :startDate="Startdate"
            :endDate="Enddate"
            title="OT-HeadCounts"
        /></v-row>

        <v-row>
          <v-col><h2>Alert List</h2></v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card flat>
              <template v-slot:text>
                <v-text-field
                  v-model="search"
                  label="Search"
                  prepend-inner-icon="mdi-magnify"
                  variant="outlined"
                  hide-details
                  single-line
                ></v-text-field>
              </template>
              <DataTable
                :show-headers="headers2"
                :items="testData"
                :search="search"
              />
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </SideBar>
  </v-app>
</template>

<script>
import SideBar from "../components/SideBar.vue";
import SelectBox from "../components/SelectBox.vue";
import WorkSummaryCard from "../components/SummaryCard.vue";
import DataTable from "../components/DataTable.vue";
import { ref } from "vue";

import BarChart from "../components/BarChart.vue";

export default {
  name: "MyTeam",
  components: {
    SideBar,
    WorkSummaryCard,
    DataTable,
    SelectBox,
    BarChart,
  },
  setup() {
    const selectedDepartment = ref("All");
    const Startdate = ref();
    const Enddate = ref();
    const startDatePicker = ref(null);
    const endDatePicker = ref(null);
    const granularity = ref("");

    const headers = [
      { text: "Total Work Hours", value: "TotalWorkHours" },
      { text: "Total OT Hours", value: "TotalOTHours" },
      { text: "OT Hours/ person", value: "OTHoursPerson" },
      { text: "OT-HeadCounts", value: "OTHeadcounts" },
    ];
    const headers2 = [
      { text: "Employee ID", value: "EmployeeID" },
      { text: "Name", value: "Name" },
      { text: "OT Counts", value: "OTCounts" },
      { text: "OT Hours", value: "OTHours" },
      { text: "Status", value: "status" },
    ];
    const Department = [
      "All",
      "Sales",
      "Marketing",
      "Human Resources",
      "Engineering",
      "Customer Support",
      "Finance",
    ];
    const summary = [
      {
        TotalWorkHours: "5649",
        TotalOTHours: "369",
        OTHoursPerson: "12.3",
        OTHeadcounts: "7",
      },
    ];
    const testData = [
      {
        EmployeeID: "E001",
        Name: "John Doe",
        OTCounts: 5,
        OTHours: 20,
        status: "Warning",
      },
      {
        EmployeeID: "E002",
        Name: "Jane Smith",
        OTCounts: 3,
        OTHours: 15,
        status: "Warning",
      },
      {
        EmployeeID: "E003",
        Name: "Mike Johnson",
        OTCounts: 8,
        OTHours: 32,
        status: "Alert",
      },
      {
        EmployeeID: "E004",
        Name: "Sarah Lee",
        OTCounts: 2,
        OTHours: 10,
        status: "Alert",
      },
    ];

    const LabelData = ["2024-04/W4", "2024-04/W5", "2024-05/W1"];
    const data = [10, 5, 7];

    return {
      selectedDepartment,
      Department,
      headers,
      headers2,
      summary,
      testData,
      Startdate,
      Enddate,
      startDatePicker,
      endDatePicker,
      LabelData,
      granularity,
      data,
    };
  },
};
</script>

<style>
.v-table .text-center td {
  justify-content: center;
}

.filter {
  display: grid;
  grid-template-columns: auto 1fr auto auto auto;
  align-items: center;
  gap: 16px;
  margin-bottom: 10px;
}

.filter2 {
  display: grid;
  grid-template-columns: auto auto 1fr;
  align-items: center;
  gap: 16px;
  margin-bottom: 10px;
}

.datepicker-container {
  width: 100%;
  max-width: 200px;
  min-width: 180px;
}

.custom-datepicker .dp__input {
  width: 100%;
  box-sizing: border-box;
  height: 40px;
  font-size: 14px;
}

.custom-datepicker .dp__menu {
  min-width: unset;
}
</style>
