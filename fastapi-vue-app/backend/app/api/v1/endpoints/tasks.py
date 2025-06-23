from uuid import UUID
from fastapi import APIRouter, Depends
from models import Task
from api.dependencies import get_db
from services import TaskService

from pymongo.asynchronous.database import AsyncDatabase

router = APIRouter()


@router.post("/")
async def create_task(task: Task, db: AsyncDatabase = Depends(get_db)):
    return await TaskService(db).create(task=task)


@router.get("/", response_model=list[Task])
async def read_tasks(
    skip: int = 0, limit: int = 10, db: AsyncDatabase = Depends(get_db)
):
    return await TaskService(db).fetch_all(skip=skip, limit=limit)


@router.get("/{task_id}", response_model=Task)
async def read_task(task_id: UUID, db: AsyncDatabase = Depends(get_db)):
    return await TaskService(db).fetch(task_id=task_id)


@router.put("/{task_id}", response_model=bool)
async def update_task(task_id: UUID, task: Task, db: AsyncDatabase = Depends(get_db)):
    return await TaskService(db).update(task_id=task_id, task=task)


@router.get("/daily/{date}", response_model=list[Task])
async def read_daily_tasks(date: str, db: AsyncDatabase = Depends(get_db)):
    return await TaskService(db).fetch_daily(date=date)
