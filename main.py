from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Todo

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to "https://your-frontend.vercel.app"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory task list
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
    return {"message": "Todo deleted"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {"message": "Todo updated", "todo": updated_todo}
    return {"error": "Todo not found"}

