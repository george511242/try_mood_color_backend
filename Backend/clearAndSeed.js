// 載入 .env 設定 (請確保專案根目錄有 .env 檔案，裡面定義了 MONGO_URI)
const config = require("./config/config");

const mongoose = require("mongoose");
const { Schema } = mongoose;

// 定義 Todo schema
const todoSchema = new Schema({
  _id: { type: String, required: true },
  text: { type: String, required: true },
  done: { type: Boolean, default: false },
});

// 建立模型
const Todo = mongoose.model("Todo", todoSchema);

async function clearAndSeed() {
  try {
    // 連線 MongoDB (mongoose 6+ 版本不需要額外選項)
    await mongoose.connect(config.DB);
    console.log("MongoDB 連線成功！");

    // 清空 Todo collection 中所有文件
    await Todo.deleteMany({});
    console.log("所有 Todo 資料已清空！");

    // 定義要新增的預設 Todo 資料
    const seedTodos = [
      {
        _id: new Date().toISOString(),
        text: "學習 Mongoose",
        done: false,
      },
      {
        _id: new Date(Date.now() + 1000).toISOString(),
        text: "撰寫重跑資料腳本",
        done: false,
      },
    ];

    // 新增預設資料
    const result = await Todo.insertMany(seedTodos);
    console.log("預設資料已新增：", result);
  } catch (error) {
    console.error("發生錯誤：", error);
  } finally {
    await mongoose.disconnect();
    console.log("MongoDB 連線已關閉");
  }
}

clearAndSeed();
