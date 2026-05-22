# 📘 Assignment: FastAPI + SQLite Persistent CRUD API

## 🎯 Objective

Build a REST API with FastAPI that stores data in a SQLite database so records persist between server restarts.

## 📝 Tasks

### 🛠️	Set Up SQLite and Read Endpoints

#### Description
Create a SQLite database for a `tasks` table and build API routes to list tasks and fetch one task by ID.

#### Requirements
Completed program should:

- Create a SQLite database file and a `tasks` table with columns `id`, `title`, `done`, and `priority`.
- Implement a `GET /tasks` endpoint that returns all tasks from the database.
- Implement a `GET /tasks/{task_id}` endpoint that returns one task by ID.
- Return a 404 error when a task ID is not found.


### 🛠️	Implement Persistent Create, Update, and Delete

#### Description
Add routes that insert, modify, and remove tasks in SQLite so all CRUD operations use the database instead of in-memory Python dictionaries.

#### Requirements
Completed program should:

- Implement `POST /tasks` to insert a new task and return the created row with its ID.
- Implement `PUT /tasks/{task_id}` to update an existing task.
- Implement `DELETE /tasks/{task_id}` to remove a task.
- Validate request data using a Pydantic model.
- Demonstrate that data remains available after restarting the server.
