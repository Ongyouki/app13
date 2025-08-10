from sqlmodel import Session, select

from app.core.db import engine
from app.models.transaction import JournalEntry


def create_journal_entry(entry: JournalEntry) -> JournalEntry:
    """Persist a journal entry and its lines."""
    with Session(engine) as session:
        session.add(entry)
        session.commit()
        session.refresh(entry)
        return entry


def list_journal_entries() -> list[JournalEntry]:
    """Retrieve all journal entries."""
    with Session(engine) as session:
        return session.exec(select(JournalEntry)).all()
