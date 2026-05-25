from fastapi import FastAPI


app=FastAPI()
items=[
    {"id":1, "name":"Betselot"},
    {"id":2, "name":"Tamene"},
    {"id":3, "name":"Getachew"},
]
@app.get("/health")
def health_check():
    return {"status": "OK"}


@app.get("/items")
def getItems():
    return items

@app.get("/items/{item_id}")
def getItems(item_i: int):
    for item in items:
        if item["id"]==item_i:
            return item
    return {"error": "item not found"}

@app.post("/items")
def create_post(item: dict):
    items.append(item)
    return item









# Decorator
# It connects a URL endpoint to a function.
# Meaning:
# when someone visits:
# /health
# using:
# GET request
# FastAPI runs the function below it.
# What is GET?
# HTTP methods:
# GET → receive data
# POST → send data
# PUT → update data
# DELETE → delete data
# What is Swagger?

# Swagger UI is a visual interface for testing and documenting APIs.

# It gives you a webpage where you can:

# see all API endpoints
# test APIs
# send requests
# view responses
# understand parameters

# without writing code manually.
