from models import Todo  # instead of from .models
from database import todos


def get_all_todos():
    return todos

def add_todo(todo: Todo):
    todos.append(todo)
    return todo

def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Todo deleted"}
