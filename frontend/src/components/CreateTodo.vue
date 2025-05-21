<template>
  <div class="col align-self-center">
    <h1>Todo List</h1>
    <fieldset>
      <input
        class="input-task"
        placeholder="Add a new task "
        v-model="name"
        @keyup.enter="addTodo($event)"
        @keypress="typing = true"
      />
      <button class="button-1" type="submit" @click="addTodo($event)">
        Add
      </button>
    </fieldset>
  </div>
</template>

<script>
import { ref } from "vue";
import { bus } from "./../bus.js";

export default {
  setup() {
    const name = ref("");
    const typing = ref(false);
    const todos = ref([]);
    const backendUrl = process.env.VUE_APP_BACKEND_URL;

    const addTodo = async (event) => {
      if (event) event.preventDefault();

      let todo = {
        id: Date.now().toString(),
        text: name.value,
        done: false,
      };
      console.log(todo);

      try {
        refreshTodo(todo);
        const response = await fetch(`${backendUrl}/todos`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(todo),
        });

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        await response.json();
        clearTodo();
        typing.value = false;
      } catch (error) {
        console.log("There was a problem with the fetch operation:", error);
      }
    };

    const fetchTodo = async () => {
      try {
        const response = await fetch(`${backendUrl}/todos`);
        const data = await response.json();
        todos.value = data;
      } catch (error) {
        console.error("獲取失敗:", error);
      }
    };

    const clearTodo = () => {
      name.value = "";
    };

    const refreshTodo = (newTodo) => {
      bus.emit("refreshTodo", newTodo);
    };

    return {
      name,
      typing,
      todos,
      addTodo,
      fetchTodo,
      clearTodo,
      refreshTodo,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
fieldset {
  border: none;
  padding: 2px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.input-task {
  width: 50%;
  height: 30px;
  margin-right: 10px;
}
.button-1 {
  width: 70px;
  height: 34px;
}
</style>
