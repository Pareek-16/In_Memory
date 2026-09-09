from fastapi import FastAPI, HTTPException

app = FastAPI()

# For simplicity, we will use an in-memory list to store items. In a real-world application, you would typically use a database.
items = []


# Home page
@app.get("/")
def home():
    return {"message": "Welcome to Inventory API"}


# Add an item
@app.post("/items")
def add_item(name: str, quantity: int, price: float):

    item = {
        "id": len(items) + 1,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    items.append(item)

    return {
        "message": "Item added successfully",
        "item": item
    }


# Get all items
@app.get("/items")
def get_items():
    return items


# Get a single item
@app.get("/items/{item_id}")
def get_item(item_id: int):

    for item in items:
        if item["id"] == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )


# Update an item
@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    name: str,
    quantity: int,
    price: float
):

    for item in items:

        if item["id"] == item_id:

            item["name"] = name
            item["quantity"] = quantity
            item["price"] = price

            return {
                "message": "Item updated successfully",
                "item": item
            }

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )


# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    for item in items:

        if item["id"] == item_id:

            items.remove(item)

            return {
                "message": "Item deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )