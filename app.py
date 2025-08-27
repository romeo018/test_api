from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return FileResponse("index.html")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"ты ввел = ": item_id, "q": q}


@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
def add(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply/{a}/{b}")
def add(a: float, b: float):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def add(a: float, b: float):
    if b == 0:
        return {"error": "Деление на ноль"}
    return {"result": a / b}

@app.get("/users")
def get_users():
    return {"users": ["user1", "user2", "user3"]}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
