const Todo = require("../models/todo");

class TodoRepository {
  constructor(model) {
    this.model = model;
  }
  create(id, name) {
    const newTodo = { _id: id, text: name, done: false };
    const todo = new this.model(newTodo);
    return todo.save();
  }

  findAll() {
    return this.model.find();
  }

  deleteByID(id) {
    return this.model.findByIdAndDelete(id);
  }
}

module.exports = new TodoRepository(Todo);
