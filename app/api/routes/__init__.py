# app/api/routes/__init__.py
from fastapi import APIRouter

from app.api.routes.chart import router as chart_router
from app.api.routes.transactions import router as transactions_router

router = APIRouter()
router.include_router(chart_router)
router.include_router(transactions_router)

__all__ = ["router"]
