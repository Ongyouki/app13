from sqlmodel import Session, select

from app.core.db import engine, init_db
from app.models import (
    AccountCategory,
    ChartOfAccount,
    JournalEntry,
    JournalLine,
)


def test_journal_entry_persists_lines():
    # Ensure tables exist
    init_db()

    with Session(engine) as session:
        # create accounts
        cash = ChartOfAccount(code="100", name="Cash", category=AccountCategory.ASSET)
        revenue = ChartOfAccount(code="400", name="Revenue", category=AccountCategory.INCOME)
        session.add(cash)
        session.add(revenue)
        session.commit()
        session.refresh(cash)
        session.refresh(revenue)

        entry = JournalEntry(description="sale", lines=[
            JournalLine(account_id=cash.id, debit=100),
            JournalLine(account_id=revenue.id, credit=100),
        ])
        session.add(entry)
        session.commit()
        session.refresh(entry)

        lines = session.exec(select(JournalLine).where(JournalLine.entry_id == entry.id)).all()
        assert len(lines) == 2
        assert sum(l.debit for l in lines) == 100
        assert sum(l.credit for l in lines) == 100
