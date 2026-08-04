#main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.docs import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Schema is now managed by Alembic migrations (see /migrations),
    # not by create_all() on startup — run `alembic upgrade head` instead.
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router.router)

@app.get('/')
async def hey():
    return {"abc": "def"}