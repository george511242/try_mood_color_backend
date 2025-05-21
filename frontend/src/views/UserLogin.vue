<template>
  <div class="login-wrapper">
    <h1 class="gradient-title">Mood Color</h1>
    <div class="input-box">
      <v-card
        class="mx-auto pa-12 pb-8"
        elevation="8"
        max-width="448"
        rounded="lg"
      >
        <div class="text-subtitle-1 text-medium-emphasis">Account</div>

        <v-text-field
          density="compact"
          placeholder="Email address"
          prepend-inner-icon="mdi-email-outline"
          variant="outlined"
          v-model="email"
        ></v-text-field>

        <div
          class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
        >
          Password

          <a
            class="text-caption text-decoration-none text-blue"
            href="#"
            target="_blank"
          >
            Forgot login password?</a
          >
        </div>

        <v-text-field
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          placeholder="Enter your password"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          @click:append-inner="visible = !visible"
          v-model="password"
        ></v-text-field>

        <v-card class="mb-12" color="surface-variant" variant="tonal">
          <v-card-text class="text-medium-emphasis text-caption">
            Warning: After 3 consecutive failed login attempts, you account will
            be temporarily locked for three hours.
          </v-card-text>
        </v-card>

        <v-btn
          @click="handleLogin"
          class="mb-8"
          color="blue"
          size="large"
          variant="tonal"
          block
        >
          Log In
        </v-btn>

        <v-card-text class="text-center">
          <router-link
            class="text-blue text-decoration-none"
            to="/RegisterPage"
            target="_blank"
          >
            Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
          </router-link>
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";
import api from "@/api"; // @ 代表 src 目錄
import { useRouter } from "vue-router";

const router = useRouter();

const email = ref("");
const password = ref("");
const visible = ref(false);
//註冊

//登入
const handleLogin = async () => {
  try {
    if (!email.value || !password.value) {
      alert("請輸入電子郵件和密碼");
      return;
    }

    // 發送登入請求到後端
    const response = await api.get(
      `/api/user/login/${encodeURIComponent(email.value)}/${encodeURIComponent(
        password.value
      )}`
    );

    // 假設後端會回傳成功訊息
    if (response.data.status === "success") {
      alert("登入成功");
      const userStore = useUserStore();
      userStore.setUserId(response.data.userid);
      localStorage.setItem("userId", response.data.userid);

      router.push("/home");
    } else {
      alert("登入失敗：" + response.data.message);
    }
  } catch (error) {
    console.error("註冊錯誤", error);
    alert("註冊時發生錯誤，請稍後再試");
  }
};
</script>

<style scoped>
.login-wrapper {
  background: linear-gradient(135deg, #a8e6cf, #56ab2f); /* 綠色漸層 */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  gap: 10px;
}
.gradient-title {
  font-size: 70px;
  font-weight: bold;
  text-align: center;

  background: linear-gradient(90deg, #ec008c, #fcb7d4); /* 粉紅漸層 */
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;

  margin-bottom: 24px;
}
</style>
