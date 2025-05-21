<template>
  <div class="todo-list">
    <div v-for="todo in todos" :key="todo._id" class="todo-item">
      <div class="todo-content">
        <input type="checkbox" :value="todo._id" v-model="selectedIndexes" />
        <span :class="{ done: todo.done }">{{ todo.text }}</span>
      </div>
    </div>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
import { ref, onMounted, watch } from "vue";
import { bus } from "./../bus.js";

export default {
  setup() {
    const todos = ref([]);
    const backendUrl = process.env.VUE_APP_BACKEND_URL;

    const selectedIndexes = ref([]);

    const fetchTodo = async () => {
      try {
        const response = await fetch(`${backendUrl}/todos`);
        const data = await response.json();
        todos.value = data;
      } catch (error) {
        console.error("錯誤");
      }
    };

    watch(selectedIndexes, (newSelectedIndexes) => {
      console.log("Updated selectedIndexes:", newSelectedIndexes);
      // 遍歷 todos，將已選擇的 todo 設為 done = true
      todos.value.forEach((todo) => {
        todo.done = newSelectedIndexes.includes(todo._id);
      });
    });

    const deleteTodo = async () => {
      try {
        await Promise.all(
          selectedIndexes.value.map((id) =>
            fetch(`${backendUrl}/todos/${id}`, { method: "DELETE" })
          )
        );

        todos.value = todos.value.filter(
          (todo) => !selectedIndexes.value.includes(todo._id)
        );
        selectedIndexes.value = [];
      } catch (error) {
        console.error("錯誤");
      }
    };
    const addTodo = (newTodo) => {
      // 將新的 todo 加入到 todos 列表中
      console.log(newTodo);
      todos.value.push(newTodo);
    };

    onMounted(() => {
      fetchTodo();
      listenToEvents();
    });

    const listenToEvents = () => {
      bus.on("refreshTodo", addTodo);
    };

    return {
      todos,
      fetchTodo,
      deleteTodo,
      selectedIndexes,
    };
  },
};
</script>

<style>
.done {
  text-decoration: line-through;
  color: grey;
}

.todo-list {
  display: block;
  width: 60%;
  margin: 5px auto;
}

.todo-item {
  display: flex;
  margin: 10px;
  padding: 10px;
  justify-content: space-between;
  background-color: #f0f0f0;
  border-radius: 5px;
}
button {
  background-color: #bfecff;
  border: 1px solid black;
  padding: 2px;
  border-radius: 4px;
  height: 34px;
  width: 70px;
}
</style>
