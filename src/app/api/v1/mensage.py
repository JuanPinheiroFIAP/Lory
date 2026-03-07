from fastapi import APIRouter, Request

chat_message = APIRouter(prefix="/webhooks", tags=["webhooks"])


@chat_message.post("/whatsapp")
async def receive_wpp_message(request: Request):
    data = await request.json()

    # Verifica se é uma mensagem recebida
    if data.get("event") == "MESSAGES_UPSERT":
        message_body = data["data"]["message"]["conversation"]
        sender_number = data["data"]["key"]["remoteJid"]

        print(f"Mensagem de {sender_number}: {message_body}")

    return {"status": "success"}
