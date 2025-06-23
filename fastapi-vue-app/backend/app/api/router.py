from fastapi import APIRouter

from .v1.endpoints import tasks
from .v1.endpoints import config

router = APIRouter()

router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
router.include_router(config.router, prefix="/config", tags=["config"])
