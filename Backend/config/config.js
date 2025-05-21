require("dotenv").config(); // 載入環境變數

const username = process.env.DB_USERNAME;
const password = process.env.DB_PASSWORD;

module.exports = {
  DB: `mongodb+srv://${username}:${password}@cluster0.fmhe6v9.mongodb.net/?retryWrites=true&w=majority`, // 優先使用 .env 中的 MONGO_URL，若無則使用預設值
  APP_PORT: process.env.APP_PORT || 80, // 優先使用 .env 中的 APP_PORT，若無則使用預設值
};
