from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price : float
    genre: str
    auther: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price : Optional[float] = None
    genre: Optional[str] = None
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
    raise HTTPException(status_code = 404, detail="The book you were searching was not found")
    #return {"Data": "The book you were searching was not found"}

@app.get("/get-by-auther_optional", summary = "Optional parameters")
def get_item2(auther:Optional[str] = None):
    for id in books:
        if books[id]["auther"] == auther:
            return books[id]
    raise HTTPException(status_code = 404, detail="The book you were searching was not found")
    #return {"Data": "The book you were searching was not found"}

@app.post("/add-book/{book_id}")
def add_book(book_id:int, item: Item):
    if book_id in books:
        #return {"Error": "Book ID already exists"}
        raise HTTPException(status_code = 405, detail="Book ID already exists")
    books[book_id] = {"name" : item.name, "price" : item.price, "genre" : item.genre, "auther" : item.auther}
    #books[book_id] = item
    return books[book_id]

@app.put("/update-book/{book_id}")
def update_book(book_id:int, item: UpdateItem):
    if book_id not in books:
        #return {"Error": "Book Id doesn't exists"}
        raise HTTPException(status_code = 404, detail="Book Id doesn't exists")

    if item.name != None:
        books[book_id]["name"] = item.name
    if item.price != None:
        books[book_id]["price"] = item.price
    if item.genre != None:
        books[book_id]["genre"] = item.genre
    if item.auther != None:
        books[book_id]["auther"] = item.auther

    return books[book_id]

@app.delete("/delete-book")
def delete_book(book_id:int):
    if book_id not in books:
        #return {"Error":"Book Id doesn't exists"}
        raise HTTPException(status_code = 404, detail="Book Id doesn't exists")

    del books[book_id]
    return {"Result": "The Book deleted"}