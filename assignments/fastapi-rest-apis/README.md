# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework and practice creating endpoints for create, read, update, and delete operations.

## 📝 Tasks

### 🛠️	Create API Models and Read Endpoints

#### Description
Set up a FastAPI project with a Pydantic model for items, then implement endpoints to view all items and retrieve a single item by ID.

#### Requirements
Completed program should:

- Define a Pydantic model named `Item` with fields for `name`, `description`, and `price`.
- Create a `GET /items` endpoint that returns a list of all items.
- Create a `GET /items/{item_id}` endpoint that returns one item by ID.
- Return a 404 error when a requested item ID does not exist.


### 🛠️	Implement Create, Update, and Delete Endpoints

#### Description
Expand the API to support full CRUD functionality by adding routes to create, update, and delete items in an in-memory data store.

#### Requirements
Completed program should:

- Create a `POST /items` endpoint that adds a new item and returns it with an ID.
- Create a `PUT /items/{item_id}` endpoint that updates an existing item.
- Create a `DELETE /items/{item_id}` endpoint that removes an item.
- Return clear success or error responses for each operation.
- Demonstrate all endpoints working using the `/docs` Swagger UI.
