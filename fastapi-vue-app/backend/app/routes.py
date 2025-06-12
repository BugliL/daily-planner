from fastapi import APIRouter, HTTPException, Depends
from models import Task
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/tasks/", response_model=Task)
def create_task(task: Task, db: Session =Depends(get_db())):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/tasks/", response_model=list[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session =Depends(get_db())):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks

@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session =Depends(get_db())):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task, db: Session =Depends(get_db())):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session =Depends(get_db())):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return {"detail": "Task deleted"}