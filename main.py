#main.py
from fastapi import FastAPI
from app.docs import router
from contextlib import asynccontextmanager
from app.db.base import Base
from app.db.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI()

app.include_router(router.router)

@app.get('/')
async def hey():
    return {"abc": "def"}

