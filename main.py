from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="First FastAPI example")
async def my_first_get_api():
    return {"message":"First FastAPI example"}