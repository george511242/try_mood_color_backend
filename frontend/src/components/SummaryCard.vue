<template>
  <div class="displayAll">
    <h3 class="display">
      {{ totalWorkHours }}
      <p class="Note">{{ unit }}</p>
      <span :style="{ color: arrowColor, marginLeft: '10px' }">
        {{ arrowSymbol }}
      </span>
    </h3>
    <p class="d Note">last {{ timeUnit }}: {{ lastRecord }} {{ unit }}</p>
  </div>
</template>

<script>
export default {
  name: "WorkSummaryCard",
  props: {
    totalWorkHours: {
      type: [String, Number],
      required: true,
    },
    unit: {
      type: String,
      required: true,
    },
    timeUnit: {
      type: String,
      required: true,
    },
    lastRecord: {
      type: [String, Number],
      required: true,
    },
  },
  computed: {
    arrowSymbol() {
      if (Number(this.totalWorkHours) > Number(this.lastRecord)) {
        return "↑"; // 上升
      } else if (Number(this.totalWorkHours) < Number(this.lastRecord)) {
        return "↓"; // 下降
      } else {
        return "-"; // 相同
      }
    },
    arrowColor() {
      if (Number(this.totalWorkHours) > Number(this.lastRecord)) {
        return "red";
      } else if (Number(this.totalWorkHours) < Number(this.lastRecord)) {
        return "green";
      } else {
        return "gray";
      }
    },
  },
};
</script>

<style>
.displayAll {
  display: inline-block; /* 讓 <div> 受 text-align 影響 */
  text-align: center;
  width: 100px;
  height: 100px;
  padding: 10px;
}
.display {
  display: flex;
  align-items: end; /* 靠左對齊 */
  font-size: 30px; /* 修正：text-size 應為 font-size */
  margin: 1px; /* 修正：margine 應為 margin */
  width: 100%;
}
.Note {
  color: grey;
  font-size: 9px;
}
.d {
  margin-top: 10px;
  display: flex;
  justify-content: center;
}
</style>
