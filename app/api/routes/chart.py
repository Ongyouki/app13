# app/api/routes/chart.py
from fastapi import APIRouter
from app.models.chart_of_account import ChartOfAccount
from app.services.chart_service import create_account, get_all_accounts

router = APIRouter(prefix="/chart", tags=["Chart of Accounts"])

@router.post("/")
def create_chart_entry(account: ChartOfAccount):
    return create_account(account)

@router.get("/")
def list_accounts():
    return get_all_accounts()
