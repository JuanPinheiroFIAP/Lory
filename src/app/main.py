from fastapi import FastAPI

from src.app.api import chat_message


app = FastAPI(title="Lory")


@app.get("/")
async def health_check():
    return {"status": "ok", "service": "Lory"}


app.include_router(chat_message)
