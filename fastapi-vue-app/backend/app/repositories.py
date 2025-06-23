from typing import Iterable, Optional
from uuid import UUID
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.errors import DuplicateKeyError
from pymongo.results import UpdateResult

from models import Task


class TaskRepository:
    COLLECTION_NAME = "tasks"

    def __init__(self, db: AsyncDatabase):
        self.collection = db.get_collection(self.COLLECTION_NAME)

    async def add(self, task: Task) -> bool:
        try:
            result = await self.collection.insert_one(
                task.model_dump(
                    mode="json",
                    by_alias=True,
                )
            )
            return bool(result.inserted_id)
        except DuplicateKeyError:
            return False

    async def get(self, task_id: str | UUID) -> Optional[Task]:
        doc = await self.collection.find_one({"_id": str(task_id)})
        return Task.model_validate(doc) if doc else None

    async def list(self, skip: int = 0, limit: int = 10) -> Iterable[Task]:
        docs = await self.collection.find().skip(skip).limit(limit).to_list(length=None)
        return map(Task.model_validate, docs)

    async def update(self, task_id: UUID | str, task: Task) -> bool:
        task_data = task.model_dump(
            mode="json",
            by_alias=True,
            exclude={"id", "_id", "created_at"},
        )

        result: UpdateResult = await self.collection.update_one(
            {"_id": str(task_id)},
            {"$set": task_data},
        )
        return bool(result.modified_count)

    async def delete(self, task_id: str | UUID) -> bool:
        result = await self.collection.delete_one({"_id": str(task_id)})
        return bool(result.deleted_count)

    async def get_daily(self, date: str) -> Iterable[Task]:
        """
        Fetch tasks for a specific date.
        The date format should be 'YYYY-MM-DD'.
        """
        docs = await self.collection.find({"task_date": date}).to_list(length=None)
        return map(Task.model_validate, docs)
