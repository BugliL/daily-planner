from fastapi import HTTPException
from uuid import UUID
from pymongo import AsyncMongoClient
from models import Task
from pymongo.asynchronous.database import AsyncDatabase

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


class DatabaseService:
    """
    A service class to handle database operations.
    This class can be extended to include more complex queries or transactions.
    """

    def __init__(self, db: AsyncDatabase):
        self.db = db

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

    async def insert_task(self, task: Task) -> UUID | None:
        """
        Create a new task in the self.db.
        """
        collection = self.db.get_collection("tasks")
        result = await collection.insert_one(
            task.model_dump(mode="json", by_alias=True)
        )
        return task.id if result.inserted_id else None

    async def fetch_all_tasks(self, skip: int = 0, limit: int = 10) -> list[Task]:
        """
        Retrieve tasks from the database with pagination.
        """
        collection = self.db.get_collection("tasks")
        cursor = collection.find({}).skip(skip).limit(limit)
        tasks = await cursor.to_list(length=limit)
        return [Task(**task) for task in tasks]

    async def fetch_task_by_id(self, task_id: UUID) -> Task | None:
        """
        Retrieve a task by its ID.
        """
        collection = self.db.get_collection("tasks")
        task = await collection.find_one({"_id": str(task_id)})
        return Task(**task) if task else None

    async def update_task(self, task_id: UUID, task: Task) -> Task | None:
        """
        Update an existing task in the self.db.
        """
        collection = self.db.get_collection("tasks")
        task_data = task.model_dump(
            mode="json",
            exclude_none=True,
            exclude={"id", "created_at"},
        )

        result = await collection.update_one(
            {"_id": str(task_id)},
            {"$set": task_data},
        )

        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Task not found")

        return await self.fetch_task_by_id(task_id=task_id)
