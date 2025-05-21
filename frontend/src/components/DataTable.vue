<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :search="search"
    class="elevation-1 text-center custom-header-center td-border-style"
  >
    <template #[`item.status`]="{ item }">
      <StatusCard :content="item.status" />
    </template>
  </v-data-table>
</template>

<script>
import StatusCard from "./StatusCard.vue";

export default {
  name: "DataTable",
  components: {
    StatusCard,
  },
  props: {
    headers: {
      type: Array,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    },
    search: {
      type: String,
      default: "",
    },
  },
};
</script>

<style scoped>
:deep(.v-data-table__th) {
  background-color: #f5f5f5 !important;
  justify-content: center;
}

:deep(.v-data-table-header__content) {
  justify-content: center;
}

#input-v-66 {
  margin-bottom: 16px; /* 想要多大空間自己調，比如16px */
}
</style>
