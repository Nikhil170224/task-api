from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.schemas import TaskCreate2,TaskUpdate,TaskOut2,TaskOut,TaskPatch,TaskCreate 

router = APIRouter(prefix="/tasks", tags=["tasks"])

tasks = [
    {"id": 1, "title": "Learn Python", "done": True},
    {"id": 2, "title": "Learn FastAPI", "done": False},
    {"id": 3, "title": "Build task API", "done": False},
]

# @router.get("/{task_id}")
# def get_task1(task_id: int):
#     for task in tasks:
#         if task["id"] == task_id:
#             return task
#     return {"error": "Task not found"}


# lesson 13 Path Param - Task 1 & 2 :

# @router.get("")
# def list_tasks1(done: bool | None = None, limit: int = 10):
#     result = tasks
#     if done is not None:
#         result = [t for t in result if t["done"] == done]
#     return result[:limit]

# -----------------------------------------


# class TaskCreate(BaseModel):
#     title: str
#     done: bool = False

# @router.post("")
# def create_task(task: TaskCreate):
#     new_id = len(tasks) + 1
#     new_task = {"id": new_id, "title": task.title, "done": task.done}
#     tasks.append(new_task)
#     return new_task

# ---------------------------------

# Lesson 15 — Validation Rules with Field:



# @router.post("", status_code=201)
# def create_task1(task: TaskCreate2):
#     new_id = len(tasks) + 1
#     new_task = {"id": new_id, "title": task.title, "done": task.done}
#     tasks.append(new_task)
#     return new_task


# ---------------------------------

# Lesson 16 — HTTPException + Status Codes

# tasks = [
#     {"id": 1, "title": "Learn Python", "done": True},
#     {"id": 2, "title": "Learn FastAPI", "done": False},
#     {"id": 3, "title": "Build task API", "done": False},
# ]

# @app.get("/tasks/{task_id}")
# def get_task(task_id: int):
#     for task in tasks:
#         if task["id"] == task_id:
#             return task
#     raise HTTPException(status_code=404, detail="Task not found")

# ---------------------------------

# Lesson 17 — PUT + DELETE (completing CRUD)

# Task 1 : TaskUpdate model


@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = task.title
            t["done"] = task.done
            return t
    raise HTTPException(status_code=404, detail="Task not found")

# Task 2 : Delete

@router.delete("/{task_id}")
def delete_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

# ---------------------------------

# Lesson 18 — Response Model

# @router.get("", response_model=list[TaskOut2])
# def list_tasks2():
#     return tasks

# @router.post("", response_model=TaskOut2, status_code=201)
# def create_task2(task: TaskCreate2):
#     task_id= len(tasks) + 1
#     new_task = {"id":task_id, "title": task.title, "done": task.done}
#     tasks.append(new_task)
#     return new_task

@router.get("/{task_id}", response_model=TaskOut2)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# Lesson 19 — PATCH (Partial Update)

@router.patch("/{task_id}", response_model=TaskOut)
def patch_task(task_id: int, task: TaskPatch):
    for t in tasks:
        if t["id"] == task_id:
            if task.title is not None:
                t["title"] = task.title
            if task.done is not None:
                t["done"] = task.done
            return t
    raise HTTPException(status_code=404, detail="Task not found")

# Lesson 20 — Pagination (skip + limit) + Search (q)

@router.post("", response_model=TaskOut, status_code=201)
def create_task(task: TaskCreate):
    task_id= len(tasks) + 1
    new_task = {"id":task_id, "title": task.title, "done": task.done}
    tasks.append(new_task)
    return new_task

@router.get("", response_model=list[TaskOut])
def list_tasks(done: bool | None = None, q: str | None = None, skip: int = 0,  limit: int = 10):
    result = tasks
    if done is not None:
        result = [t for t in result if t["done"] == done]
    if q is not None:
        result = [t for t in result if q.lower() in t["title"].lower()]
    
    return result[skip: skip + limit]