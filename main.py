from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Todo

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = []

@app.get("/todos/")
def get_todos():
    return todos

@app.post("/todos/")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Deleted"}

