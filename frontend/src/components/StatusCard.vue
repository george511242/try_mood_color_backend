<template>
  <v-card
    :class="statusClass"
    variant="tonal"
    color="black"
    style="margin: 10px"
    flat
  >
    <v-card-text
      style="display: flex; align-items: center; justify-content: center"
    >
      {{ content }}
    </v-card-text>
  </v-card>
</template>

<script setup>
import { computed, defineProps } from "vue";

const props = defineProps({
  content: {
    type: String,
    required: true,
  },
});

// 使用 computed 判斷 content，並返回相對應的類名
const statusClass = computed(() => {
  switch (props.content) {
    case "On Time":
      return "on-time";
    case "Late":
      return "late";
    case "Leave Early":
      return "leave-early";
    case "Absent":
      return "absent";
    case "Abnormal":
      return "abnormal";
    case "Day Off":
      return "day-off";
    case "Alert":
      return "alert"; // 改為小寫開頭，以符合 CSS class 通常的小寫格式
    case "Warning":
      return "warning"; // 同上，改為小寫
    default:
      return ""; // 提供一個預設的類名，方便調試
  }
});
</script>

<style scoped>
.on-time {
  background-color: rgba(30, 154, 108, 0.3); /* 綠色 */
}

.late {
  background-color: rgba(223, 155, 8, 0.3); /* 橘黃色 */
}

.leave-early {
  background-color: rgba(255, 165, 0, 0.3); /* 淺橘色 */
}

.absent {
  background-color: rgba(255, 0, 0, 0.3); /* 紅色 */
}

.abnormal {
  background-color: rgba(96, 96, 96, 0.3); /* 灰色 */
}

.day-off {
  background-color: transparent;
  color: #666666;
}
.alert {
  background-color: #fcd12a;
}
.warning {
  background-color: red;
}
</style>
