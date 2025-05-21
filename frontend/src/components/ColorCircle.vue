<template>
  <v-card class="square-card" elevation="3">
    <v-card-title>Your color of today</v-card-title>
    <v-card-subtitle>{{ formattedDate }}</v-card-subtitle>

    <v-card-text class="fixed-width-card-text">
      <div class="circle" :style="{ backgroundColor: computedColor }"></div>
      <br />
      <div class="text-below-circle">{{ text }}</div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "ColorCircle",
  props: {
    date: String, // 傳進來的日期
    color: String, // 新增：傳進來的顏色
    text: String,
  },
  computed: {
    formattedDate() {
      return this.date || new Date().toISOString().slice(0, 10);
    },
    computedColor() {
      // 如果父層有傳顏色，優先使用；否則預設顏色
      return this.color && this.color.trim() !== "" ? this.color : "#f39c12";
    },
  },
};
</script>

<style scoped>
.square-card {
  width: 250px;
  height: 350px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  overflow-y: auto;
  
}

.circle {
  width: 110px;
  height: 110px;
  border-radius: 50%;
  margin-top: 8px;
  margin-left: auto;
  margin-right: auto;
  transition: background-color 0.3s;
  border: 1px solid black;
}


/* .text-below-circle {
  text-align: center;
  margin-top: 8px;
  font-size: 14px;
  color: #333;
} */
</style>
