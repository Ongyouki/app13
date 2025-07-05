# app/core/db.py
from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database.db", echo=True)

def init_db():
    from app.models.chart_of_account import ChartOfAccount  # import all models here
    SQLModel.metadata.create_all(engine)
