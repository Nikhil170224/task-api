from fastapi import FastAPI
from app.routers import tasks

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Fastapi"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/about")
def about() -> dict:
    return {"Name": "Nikhil", "Project": "task-api", "learning": "FastApi"}

# lesson 12 Path Param - Task 2 :

@app.get("/users/{name}")
def greet(name: str):
    return {"message": f"hello, {name}"}

# -----------------------------------------
app.include_router(tasks.router)