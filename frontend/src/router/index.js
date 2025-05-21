import { createRouter, createWebHistory } from "vue-router";
import UserLogin from "../views/UserLogin.vue"; // 確保這裡是引入 UserLogin

import HomePage from "../views/HomePage.vue";
import registerPage from "../views/RegisterPage.vue";
import analysis from "../views/Analysis.vue";

const routes = [
  { path: "/", name: "UserLogin", component: UserLogin }, // 使用 UserLogin 組件
  { path: "/home", name: "HomePage", component: HomePage },
  { path: "/analysis", name: " analysis", component: analysis },
  { path: "/registerPage", name: "registerPage", component: registerPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
