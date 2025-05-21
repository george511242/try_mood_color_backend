<template>
  <v-app>
    <!-- 上方 ToolBar -->
    <v-app-bar app color="white" elevation="2">
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-img
        src="@/assets/logo.png"
        max-width="40"
        max-height="32"
        class="ml-2"
        contain
      ></v-img>
      <v-toolbar-title style="font-size: 25px; font-weight: bold"
        >Your Mood Color Journey</v-toolbar-title
      >
    </v-app-bar>

    <!-- 側邊欄 Drawer -->
    <v-navigation-drawer app v-model="drawer">
      <v-list>
        <v-list-item
          button
          @click="goToTodo('/home')"
          class="d-flex align-center"
        >
          <v-icon class="mr-2">mdi-home</v-icon>
          home
        </v-list-item>

        <v-list-item
          button
          @click="goToTodo('/analysis')"
          class="d-flex align-center"
        >
          <v-icon class="mr-2">mdi-account-group</v-icon>
          Anaylsis
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- 主內容區域 -->
    <v-main>
      <v-container>
        <!-- 使用 slot 來接收父頁面傳來的內容 -->
        <slot></slot>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "TodayAttendance", // 拼字修正
  components: {},
  setup() {
    const drawer = ref(false);

    const router = useRouter();

    function goToTodo(page) {
      router.push(page);
    }

    return {
      drawer,
      goToTodo,
    };
  },
};
</script>

<style scoped>
h2 {
  margin: 10px auto;
  font-size: 30px;
}

.login-page {
  display: flex;
  flex-direction: column;
  align-items: center; /* 這樣內容（input, button）就會置中 */
  margin-top: 0px;
}
.centered-input {
  max-width: 500px;
  width: 100%;
  margin: 0 auto;
}
</style>
