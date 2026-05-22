import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI SQLite CRUD Assignment")
DB_PATH = "tasks.db"


class TaskIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    done: bool = False
    priority: int = Field(ge=1, le=5)


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL,
            priority INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"message": "Task API is running. Open /docs to test endpoints."}


@app.get("/tasks")
def list_tasks():
    conn = get_connection()
    rows = conn.execute("SELECT id, title, done, priority FROM tasks ORDER BY id").fetchall()
    conn.close()
    return [
        {
            "id": row["id"],
            "title": row["title"],
            "done": bool(row["done"]),
            "priority": row["priority"],
        }
        for row in rows
    ]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    conn = get_connection()
    row = conn.execute(
        "SELECT id, title, done, priority FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"]),
        "priority": row["priority"],
    }


@app.post("/tasks")
def create_task(task: TaskIn):
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO tasks (title, done, priority) VALUES (?, ?, ?)",
        (task.title, int(task.done), task.priority),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, **task.model_dump()}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskIn):
    conn = get_connection()
    existing = conn.execute("SELECT id FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if existing is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    conn.execute(
        "UPDATE tasks SET title = ?, done = ?, priority = ? WHERE id = ?",
        (task.title, int(task.done), task.priority, task_id),
    )
    conn.commit()
    conn.close()
    return {"id": task_id, **task.model_dump()}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_connection()
    existing = conn.execute("SELECT id FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if existing is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return {"message": "Task deleted", "id": task_id}
