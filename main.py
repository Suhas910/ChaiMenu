from fastapi import FastAPI
from data import menu_items


app = FastAPI(
    title = "Chai Point menu API",
    description = "Read only menu API for kioask, mobile, web, etc"
)

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/menu")
def menu():
    return menu_items

@app.get("/menu/items")
def items():
    all_items = []

    for item in menu_items :
        all_items.append(item["name"])

    return all_items

@app.get("/menu/category")
def menu_category(category : str):
    category_items = []

    for item in menu_items :
        if item["category"] == category :
            category_items.append(item)

    return category_items

@app.get("/menu/{id}")
def menu_item(id : int):

    for item in menu_items:
        if item["id"] == id :
            return item

