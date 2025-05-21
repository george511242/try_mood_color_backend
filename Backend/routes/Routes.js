const express = require("express");
const todoRepository = require("../repositories/todoRepository");
const app = express.Router();
const repository = require("../repositories/todoRepository");

app.get("/", (req, res) => {
  repository
    .findAll()
    .then((todos) => {
      res.json(todos);
    })
    .catch((error) => console.log(error));
});

app.post("/", (req, res) => {
  const { id, text } = req.body;
  console.log(id, text);

  repository
    .create(id, text)
    .then((todo) => {
      res.json(todo);
    })
    .catch((error) => console.log(error));
});

app.delete("/:id", (req, res) => {
  const { id } = req.params;
  repository
    .deleteByID(id)
    .then((ok) => {
      console.log(ok);
      console.log(`Deleted record with id: ${id}`);
      res.status(200).json([]);
    })
    .catch((error) => console.log(error));
});

module.exports = app;
