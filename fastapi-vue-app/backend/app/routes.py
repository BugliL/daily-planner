from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends
from models import Task
from database import fetch_all_tasks, fetch_task_by_id, get_db, insert_task

from pymongo.asynchronous.database import AsyncDatabase

router = APIRouter()


@router.get("/init/")
async def init_db(db: AsyncDatabase = Depends(get_db)):
    await db.create_collection("Days")

    # Initialize the database with some data
    return {"message": "Database initialized"}


@router.post("/tasks/")
async def create_task(task: Task, db: AsyncDatabase = Depends(get_db)):
    return await insert_task(task)


@router.get("/tasks/", response_model=list[Task])
async def read_tasks(
    skip: int = 0, limit: int = 10, db: AsyncDatabase = Depends(get_db)
):
    return await fetch_all_tasks(skip=skip, limit=limit)


@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: str, db: AsyncDatabase = Depends(get_db)):
    return await fetch_task_by_id(task_id=task_id)


@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, task: Task, db: AsyncDatabase = Depends(get_db)):
    if (db_task := await fetch_task_by_id(task_id=task_id)) is None:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task.model_dump().items():
        setattr(db_task, key, value)

    return await update_task(task_id=task_id, task=db_task)

