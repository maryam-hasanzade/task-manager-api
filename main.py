from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import engine, Base
import models
from database import SessionLocal

print("🔥 I AM RUNNING THIS MAIN.PY")

app = FastAPI()

Base.metadata.create_all(bind=engine)

class Task(BaseModel):
    title: str
    description: str

@app.get("/")
def home():
    return {"message": "Task Manager API is running!"}

@app.post("/task")
def create_task(task: Task):
    db = SessionLocal()

    new_task = models.Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    db.close()

    return new_task


@app.get("/tasks")
def get_tasks():
    db = SessionLocal()

    tasks = db.query(models.Task).all()

    db.close()

    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    db = SessionLocal()

    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    db.close()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    db = SessionLocal()

    existing_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    existing_task.title = task.title
    existing_task.description = task.description

    db.commit()
    db.refresh(existing_task)

    db.close()

    return existing_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    db.close()

    return {"message": "Task deleted successfully"}