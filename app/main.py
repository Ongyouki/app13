from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router
from app.core.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    # cleanup logic if needed

app = FastAPI(lifespan=lifespan)
app.include_router(router)