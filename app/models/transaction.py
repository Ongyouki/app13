from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.models.chart_of_account import ChartOfAccount


class JournalEntry(SQLModel, table=True):
    """Represents a single journal entry/transaction."""

    id: Optional[int] = Field(default=None, primary_key=True)
    description: Optional[str] = None
    date: datetime = Field(default_factory=datetime.utcnow)

    # relationship
    lines: List["JournalLine"] = Relationship(back_populates="entry")


class JournalLine(SQLModel, table=True):
    """Line items for a journal entry defining debit/credit amounts."""

    id: Optional[int] = Field(default=None, primary_key=True)
    entry_id: int = Field(foreign_key="journalentry.id")
    account_id: int = Field(foreign_key="chartofaccount.id")

    debit: float = 0
    credit: float = 0

    # relationships
    entry: JournalEntry = Relationship(back_populates="lines")
    account: Optional[ChartOfAccount] = Relationship()


__all__ = ["JournalEntry", "JournalLine"]
