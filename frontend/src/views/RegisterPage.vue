<template>
  <div class="login-wrapper">
    <h1 class="gradient-title">Mood Color</h1>
    <v-card
      class="mx-auto pa-12 pb-8"
      elevation="8"
      max-width="448"
      rounded="lg"
      title="User Registration"
    >
      <v-container>
        <v-text-field
          v-model="name"
          color="primary"
          label="name"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="email"
          color="primary"
          label="Email"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="password"
          color="primary"
          label="Password"
          placeholder="Enter your password"
          variant="underlined"
        ></v-text-field>
      </v-container>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn color="success" @click="register">
          Complete Registration
          <v-icon icon="mdi-chevron-right" end></v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "@/api"; // @ 代表 src 目錄
const name = ref("");
const email = ref("");
const password = ref("");
import { useRouter } from "vue-router";

const router = useRouter();

const register = async () => {
  try {
    if (!email.value || !password.value || !name.value) {
      alert("空值存在，請補齊資訊");
      return;
    }
    console.log(name.value);

    // 發送登入請求到後端
    const response = await api.post("/api/user", {
      username: name.value,
      email: email.value,
      password_hash: password.value,
    });

    // 成功
    if (response.data.message === "User created successfully") {
      alert("註冊成功");
      router.push("/");
    } else {
      alert("登入結果：" + response.data.message);
    }
  } catch (error) {
    console.error("登入錯誤", error);
    alert("登入時發生錯誤，請稍後再試");
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
