from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price : float
    genre: str
    auther: Optional[str] = None

books = {
    1:{
        "name":"The Little Prince",
        "price":5.50,
        "genre":"Children Literature",
        "auther":"Antoine de Saint-Exupéry"
    },
    2:{
        "name":"Sapiens",
        "price":9.90,
        "genre":"Nonfiction",
        "auther":"Yuval Noah Harari"
    }
}

@app.get("/", summary="First FastAPI example")
async def my_first_get_api():
    return {"message":"First FastAPI example"}

@app.get("/get-book/{book_id}", summary="FastAPI get example with parameters")
def get_item(book_id: int):
    return books[book_id]

@app.get("/get-by-auther", summary = "Get book by auther")
def get_item2(auther:str):
    for id in books:
        if books[id]["auther"] == auther:
            return books[id]
    return {"Data": "The book you were searching was not found"}

@app.get("/get-by-auther_optional", summary = "Optional parameters")
def get_item2(auther:Optional[str] = None):
    for id in books:
        if books[id]["auther"] == auther:
            return books[id]
    return {"Data": "The book you were searching was not found"}

@app.post("/add-book/{book_id}")
def add_book(book_id:int, item: Item):
    if book_id in books:
        return {"Error": "Book ID already exists"}
    books[book_id] = {"name" : item.name, "price" : item.price, "genre" : item.genre, "auther" : item.auther}
    #books[book_id] = item
    return books[book_id]