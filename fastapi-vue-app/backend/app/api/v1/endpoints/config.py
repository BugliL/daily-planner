from fastapi import APIRouter, Depends
from api.dependencies import get_db

from pymongo.asynchronous.database import AsyncDatabase
from database import DatabaseService

router = APIRouter()


@router.post("/init/")
async def init_database(db: AsyncDatabase = Depends(get_db)):
    return await DatabaseService(db).init_db()
