from uuid import UUID
from pymongo import AsyncMongoClient
from models import Task

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


async def insert_task(task: Task):
    """
    Create a new task in the database.
    """
    collection = database.get_collection("tasks")
    result = await collection.insert_one(task.model_dump(mode="json"))
    return task.id if result.inserted_id else None


async def fetch_all_tasks(skip: int = 0, limit: int = 10):
    """
    Retrieve tasks from the database with pagination.
    """
    collection = database.get_collection("tasks")
    cursor = collection.find({}).skip(skip).limit(limit)
    tasks = await cursor.to_list(length=limit)
    return [Task(**task) for task in tasks]


async def fetch_task_by_id(task_id: str):
    """
    Retrieve a task by its ID.
    """
    collection = database.get_collection("tasks")
    task = await collection.find_one({"id": task_id})
    return Task(**task) if task else None


async def update_task(task_id: str, task: Task):
    """
    Update an existing task in the database.
    """
    collection = database.get_collection("tasks")
    result = await collection.update_one(
        {"id": task_id},
        {"$set": task.model_dump(mode="json")},
    )

    if result.modified_count == 0:
        return None

    return await fetch_task_by_id(task_id)
