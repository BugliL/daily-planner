from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends
from models import Task
from database import DatabaseService, get_db

from pymongo.asynchronous.database import AsyncDatabase

router = APIRouter()


@router.get("/init/")
async def init_db(db: AsyncDatabase = Depends(get_db)):
    return await DatabaseService(db).init_db()


@router.post("/tasks/")
async def create_task(task: Task, db: AsyncDatabase = Depends(get_db)):
    return await DatabaseService(db).insert_task(task=task)


@router.get("/tasks/", response_model=list[Task])
async def read_tasks(
    skip: int = 0, limit: int = 10, db: AsyncDatabase = Depends(get_db)
):
    return await DatabaseService(db).fetch_all_tasks(skip=skip, limit=limit)


@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: UUID, db: AsyncDatabase = Depends(get_db)):
    return await DatabaseService(db).fetch_task_by_id(task_id=task_id)


@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: UUID, task: Task, db: AsyncDatabase = Depends(get_db)):
    return await DatabaseService(db).update_task(task_id=task_id, task=task)
