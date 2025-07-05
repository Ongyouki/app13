# app/api/routes/__init__.py
from fastapi import APIRouter
from app.api.routes.chart import router as chart_router

router = APIRouter()
router.include_router(chart_router)  

__all__ = ["router"]

# from app.api.routes.auth import router as auth_router
# from app.api.routes.users import router as users_router
# from app.api.routes.transactions import router as transactions_router
# router.include_router(auth_router, prefix="/auth", tags=["auth"])
# router.include_router(users_router, prefix="/users", tags=["users"])
# router.include_router(transactions_router, prefix="/transactions", tags=["transactions"])