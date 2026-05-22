from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    name: str
    description: str
    price: float


# In-memory data store for assignment practice.
items = {
    1: {"name": "Notebook", "description": "College ruled notebook", "price": 4.99},
    2: {"name": "Pen Pack", "description": "Pack of 5 blue pens", "price": 2.49},
}

next_item_id = 3


@app.get("/")
def root():
    return {"message": "Welcome! Open /docs to test the API."}


@app.get("/items")
def get_items():
    # TODO: Return all items in a useful format.
    return {"items": items}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: Return one item or raise 404 if not found.
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "item": items[item_id]}


@app.post("/items")
def create_item(item: Item):
    # TODO: Save the incoming item, assign an ID, and return it.
    global next_item_id
    items[next_item_id] = item.model_dump()
    created = {"id": next_item_id, "item": items[next_item_id]}
    next_item_id += 1
    return created


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # TODO: Update an existing item or raise 404 if not found.
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item.model_dump()
    return {"id": item_id, "item": items[item_id]}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: Delete an item or raise 404 if it does not exist.
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items.pop(item_id)
    return {"message": "Item deleted", "id": item_id, "item": deleted_item}
