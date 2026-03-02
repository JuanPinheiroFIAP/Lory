from fastapi import FastAPI

from src.app.api.v1.mensage import chat_message

app = FastAPI(title="Lory")

app.include_router(chat_message)
