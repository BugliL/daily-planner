from fastapi import APIRouter

from .endpoints import tasks, config

router = APIRouter()

router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
router.include_router(config.router, prefix="/config", tags=["config"])
