from fastapi import APIRouter

from app.models.transaction import JournalEntry
from app.services.transaction_service import (
    create_journal_entry,
    list_journal_entries,
)

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("/")
def create_entry(entry: JournalEntry):
    return create_journal_entry(entry)


@router.get("/")
def get_entries():
    return list_journal_entries()
