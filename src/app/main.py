from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.app.core.init_db import init_db
from src.app.api.v1.mensage import chat_message


@asynccontextmanager
async def lifespan(app: FastAPI):

    init_db()

    yield


app = FastAPI(title="Lory", lifespan=lifespan)

app.include_router(chat_message)
