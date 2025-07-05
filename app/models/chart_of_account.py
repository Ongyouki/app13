from sqlmodel import SQLModel, Field
from typing import Optional
import enum

class AccountCategory(str, enum.Enum):
    ASSET = "Asset"
    LIABILITY = "Liability"
    EQUITY = "Equity"
    INCOME = "Income"
    EXPENSE = "Expense"

class ChartOfAccount(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str  # e.g., '110' or '210'
    name: str  # e.g., 'Cash' or 'Accounts Payable'
    description: Optional[str] = None

    category: AccountCategory  # Asset, Liability, etc.
    is_heading: bool = False
    is_sub_heading: bool = False

    parent_id: Optional[int] = Field(default=None, foreign_key="chartofaccount.id")

def interpret_code(account_code: str) -> dict:
    code = int(account_code)
    return {
        "is_heading": code % 100 == 0,
        "is_sub_heading": code % 10 == 0 and code % 100 != 0,
        "category": {
            1: "Asset",
            2: "Liability",
            3: "Equity",
            4: "Income",
            5: "Expense"
        }.get(code // 100, "Unknown")
    }