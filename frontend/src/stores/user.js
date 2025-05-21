// store/user.js
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    userId: null, // 初始為 null
  }),
  actions: {
    // 設定 userId 並將其保存在 localStorage
    setUserId(id) {
      this.userId = id;
      localStorage.setItem("userId", id);
    },
    // 從 localStorage 讀取 userId
    loadUserId() {
      const storedUserId = localStorage.getItem("userId");
      if (storedUserId) {
        this.userId = storedUserId;
      }
    },
  },
});
