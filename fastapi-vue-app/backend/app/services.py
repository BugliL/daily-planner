from typing import Iterable
from uuid import UUID
from pymongo import AsyncMongoClient
from models import Task
from pymongo.asynchronous.database import AsyncDatabase
from repositories import TaskRepository

DATABASE_URL = "mongodb://localhost:27017"
DATABASE_NAME = "daily_planner"

client: AsyncMongoClient = AsyncMongoClient(DATABASE_URL)
database = client.get_database(DATABASE_NAME)


async def get_db():
    """
    Get the database connection.
    This function can be used in FastAPI dependencies
    to provide a database session.
    """
    return database


class TaskService:
    """
    A service class to handle database operations.
    This class can be extended to include more complex queries or transactions.
    """

    def __init__(self, db: AsyncDatabase):
        self.db = db
        self.repository = TaskRepository(db)

    async def init_db(self) -> dict:
        """
        Initialize the database with necessary collections.
        This function can be called at application startup.
        """

        collection_names = await self.db.list_collection_names()
        if "tasks" in collection_names:
            await self.db.tasks.drop()
            await self.db.create_collection("tasks")

        return {"message": "Database initialized"}

    async def create(self, task: Task) -> bool:
        """
        Create a new task in the self.db.
        """
        return await self.repository.add(task)

    async def fetch_all(self, skip: int = 0, limit: int = 10) -> Iterable[Task]:
        """
        Retrieve tasks from the database with pagination.
        """
        return await self.repository.list(skip=skip, limit=limit)

    async def fetch(self, task_id: UUID) -> Task | None:
        """
        Retrieve a task by its ID.
        """
        return await self.repository.get(task_id=task_id)

    async def update(self, task_id: UUID | str, task: Task) -> bool:
        """
        Update an existing task in the self.db.
        """
        return await self.repository.update(task_id=task_id, task=task)

    async def fetch_daily(self, date: str) -> Iterable[Task]:
        """
        Retrieve tasks for a specific date.
        """
        return await self.repository.get_daily(date=date)
