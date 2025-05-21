<template>
  <v-app>
    <SideBar>
      <div class="container">
        <div class="item infobar">
          <DialogBox>
            <template #content>
              <p>{{ geminiComment }}</p>
            </template>
          </DialogBox>
          <v-avatar color="red">
            <span class="text-h5">CJ</span>
          </v-avatar>
        </div>
        <div>
          <keep-alive>
            <CalenderView @update:date="fetchColorForDate" />
          </keep-alive>

          <div class="color-circle-wrapper">
            <ColorCircle :date="parentPickedDate" :color="color" :text="text" />
          </div>
        </div>

        <div class="journal">
          <h2>Date: {{ parentPickedDate }} </h2>
          <v-textarea
            label="Input"
            variant="outlined"
            style="height: 300px"
            v-model="journalText"
          ></v-textarea>
          <v-btn 
            :disabled="isLoading"  
            class="submit-button" 
            color="white" 
            @click="submitJournal"
          >
            <span v-if="isLoading">Submitting...</span> <!-- 如果正在提交，显示提交中 -->
            <span v-else>Submit</span> <!-- 否则显示普通的提交按钮 -->
          </v-btn>
        </div>
      </div>
    </SideBar>
  </v-app>
</template>

<script setup>
import { ref, onMounted } from "vue";
import SideBar from "../components/SideBar.vue";
import CalenderView from "../components/Calender.vue";
import DialogBox from "../components/Dialogs.vue";
import ColorCircle from "../components/ColorCircle.vue";
import api from "@/api";
import { useUserStore } from "@/stores/user";

const userStore = useUserStore(); // 使用 Pinia store
const userId = ref(null); // 用來存儲 userId
const isLoading = ref(false);

const parentPickedDate = ref(""); // 用戶選的日期
const journalText = ref(""); // 用戶輸入的日記內容
const color = ref(""); // 用來儲存顏色
const text = ref("");
const geminiComment = ref("");


// 預設頁面日期為今天
onMounted(() => {
  userStore.loadUserId(); // 確保讀取 userId
  userId.value = userStore.userId; // 從 store 獲取 userId

  if (!userId.value) {
    alert("用戶尚未登入");
  }
  
  // 預設為今天的日期
  const today = new Date();
  parentPickedDate.value = today.toISOString().split("T")[0]; // 格式化日期为 "YYYY-MM-DD"

  // 頁面載入時抓取今天的顏色
  fetchColorForDate(parentPickedDate.value);
});

// 通过 API 获取选定日期的颜色
const fetchColorForDate = async (selectedDate) => {
  parentPickedDate.value = selectedDate; // 更新选定的日期
  try {
    isLoading.value = true; // 启动加载状态

    // 发起请求获取该日期的颜色，使用路径参数而不是查询参数
    const response = await api.get(`/api/mood_tree_color/${userId.value}/${selectedDate}`);
    console.log("color get:", response); // ← 加這一行來觀察

    // 检查响应状态
    if (response.statusText !== "OK") {
      alert("無法獲取顏色：" + response.data.message);
      return;
    }

    // 获取并设置颜色
    color.value = response.data.hex;
    text.value = response.data.content_text;
   
    localStorage.setItem("lastColor", color.value); // 将颜色存储到 localStorage 中
    localStorage.setItem("lastText", text.value); // 将文本存储到 localStorage 中
  } catch (error) {
    console.error("獲取顏色失敗:", error);
    alert("今天還沒留下日記唷！");
  } finally {
    isLoading.value = false; // 结束加载状态
  }
};


// 提交日记
const submitJournal = async () => {
  try {
    if (!journalText.value) {
      alert("請記錄些東西再送出吧");
      return;
    }
    isLoading.value = true;

    const formData = new FormData();
    formData.append("user_id", userId.value);
    formData.append("entry_date", parentPickedDate.value);
    formData.append("content_text", journalText.value);
    formData.append("mood_icon_code", "string");

    const response = await api.post("/api/Post_diary_entry", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    if (response.data.status === "success") {
      color.value = response.data.diary_entry.hex_color_code; // 获取并更新颜色
      console.log('gemini comment:', response.data.gemini_comment);
      console.log("API response data:", response.data);

      geminiComment.value = response.data.gemini_comment;
      text.value = journalText.value; 
      localStorage.setItem("lastColor", color.value); // 存储颜色到 localStorage
      console.log("color get:", color); // ← 加這一行來觀察
      alert("日記上傳成功");
    } else {
      alert("發生錯誤：" + response.data.message);
    }
  } catch (error) {
    console.error("發生錯誤:", error);
    alert("發生錯誤，請稍後再試");
  } finally {
    isLoading.value = false;  // 完成后将 isLoading 设置为 false，重新启用按钮
  }
};
</script>


<style scoped>

.container {
  display: grid;
  margin-top: 30px;
  grid-template-columns: auto auto;
  grid-template-rows: auto  ;
  gap: 40px;
}
.item {
  grid-column: 2;
  align-self: center;
}
.infobar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}
.journal {
  display: flex;
  flex-direction: column;
  min-height: 600px;
}
.submit-button {
  width: 130px;
  align-self: flex-end;
  color: #1976d2;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
.square-card[data-v-19047e93] {
  width: 450px;
  height: 280px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
.color-circle-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

</style>
