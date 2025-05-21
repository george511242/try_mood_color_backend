import { createApp } from "vue";
import App from "./App.vue";

import router from "./router";
import vuetify from "./plugins/vuetify";
import "vuetify/styles";
import { loadFonts } from "./plugins/webfontloader";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
import { createPinia } from "pinia";

loadFonts();
const pinia = createPinia();

createApp(App)
  .use(router)
  .use(vuetify)
  .use(pinia)
  .component("VueDatePicker", VueDatePicker)
  .mount("#app");
