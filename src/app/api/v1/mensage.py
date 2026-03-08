from fastapi import APIRouter, Request

chat_message = APIRouter(prefix="/webhooks", tags=["webhooks"])


@chat_message.post("/whatsapp")
async def receive_wpp_message(request: Request):
    data = await request.json()

    print("Webhook recebido:", data)

    if data.get("event") == "MESSAGES_UPSERT":

        message_data = data["data"]["message"]
        sender_number = data["data"]["key"]["remoteJid"]

        message_body = None

        if "conversation" in message_data:
            message_body = message_data["conversation"]

        elif "extendedTextMessage" in message_data:
            message_body = message_data["extendedTextMessage"]["text"]

        if message_body:
            print(f"Mensagem de {sender_number}: {message_body}")

    return {"status": "success"}
