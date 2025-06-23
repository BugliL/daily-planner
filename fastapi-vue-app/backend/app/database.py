from pymongo import AsyncMongoClient
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
