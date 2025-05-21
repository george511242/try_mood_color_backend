<template>
  <v-select
    :items="items"
    :model-value="modelValue"
    @update:modelValue="$emit('update:modelValue', $event)"
    variant="outlined"
  ></v-select>
</template>

<script>
export default {
  name: "SelectBox",
  components: {},
  props: {
    modelValue: {
      type: String,
      default: "",
    },
    items: {
      type: Array,
      required: true,
    },
  },
};
</script>
