<template>
  <div id="calendar"></div>
</template>

<script>
import { onMounted } from "vue";
import { Calendar } from "vanilla-calendar-pro";
import "vanilla-calendar-pro/styles/index.css";
export default {
  name: "CalenderView",
  emits: ["update:date"], // Declare the event name
  setup(props, { emit }) {
    onMounted(() => {
      const calendar = new Calendar("#calendar", {
        settings: {
          lang: "en",
          selection: {
            day: "single", // Single-day selection mode
          },
        },
        onClickDate(self) {
          const selected = self.context.selectedDates?.[0];
          console.log("Clicked date:", selected);

          // Emit the date change event to the parent
          emit("update:date", selected);
        },
      });

      calendar.init(); // Initialize the calendar
      console.log("Calendar initialized");
    });
  },
};
// export default {
//   name: "CalenderView",
//   emits: ["update:date"], // Declare the event name
//   setup(props, { emit }) {
//     // Destructure emit from context
//     onMounted(() => {
//       const calendar = new Calendar("#calendar", {
//         settings: {
//           lang: "en",
//           selection: {
//             day: "single", // Single-day selection mode
//           },
//         },
//         onClickDate(self) {
//           const selected = self.context.selectedDates?.[0];
//           console.log("Clicked date:", selected);

//           // Emit the date change event to the parent
//           emit("update:date", selected);
//         },
//       });

//       calendar.init(); // Initialize the calendar
//       console.log("Calendar initialized");
//     });
//   },
// };
</script>

<style scoped>
/* You can add custom styles here */
</style>
