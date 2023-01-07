from fastapi import FastAPI

app = FastAPI()

books = {
    1:{
        "name":"The Little Prince",
        "price":5.50,
        "auther":"Antoine de Saint-Exupéry"
    },
    2:{
        "name":"Sapiens",
        "price":9.90,
        "auther":"Yuval Noah Harari"
    }
}

@app.get("/", summary="First FastAPI example")
async def my_first_get_api():
    return {"message":"First FastAPI example"}

@app.get("/get-book/{book_id}", summary="FastAPI get example with parameters")
def get_item(book_id: int):
    return books[book_id]