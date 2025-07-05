from sqlmodel import Session, select
from app.core.db import engine
from app.models.chart_of_account import ChartOfAccount

def create_account(account: ChartOfAccount):
    with Session(engine) as session:
        session.add(account)
        session.commit()
        session.refresh(account)
        return account

def get_all_accounts():
    with Session(engine) as session:
        return session.exec(select(ChartOfAccount)).all()
