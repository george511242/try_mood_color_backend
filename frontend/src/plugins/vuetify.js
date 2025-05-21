// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

import { createVuetify } from "vuetify";

export default createVuetify({
  theme: {
    themes: {
      light: {
        colors: {
          "data-table-header": "#808080", // 設定 v-data-table header 為灰色
        },
      },
    },
  },
});
