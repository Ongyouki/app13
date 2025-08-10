# app/core/db.py
from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database.db", echo=True)

def init_db():
    """Create database tables."""
    # Import models so SQLModel is aware of them
    from app.models.chart_of_account import ChartOfAccount  # noqa: F401
    from app.models.transaction import JournalEntry, JournalLine  # noqa: F401

    SQLModel.metadata.create_all(engine)
