<template>
  <div class="container">
    <div class="row vertical-centre justify-content-center mt-50">
      <CreateTodo></CreateTodo>
      <ListTodo></ListTodo>
    </div>
  </div>
</template>

<script>
import CreateTodo from "../components/CreateTodo.vue";
import ListTodo from "../components/ListTodo.vue";

export default {
  name: "TodoView",
  components: {
    CreateTodo,
    ListTodo,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
