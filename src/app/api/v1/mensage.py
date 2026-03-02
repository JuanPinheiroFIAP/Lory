from fastapi import APIRouter, Request, Response

chat_message = APIRouter(prefix="/webhooks", tags=['webhooks'])


@chat_message.post("/whatsapp")
async def receive_whatsapp_message(request: Request):
    data = await request.json()
    print(f"Mensagem recebida: {data}")
    
    # O WhatsApp exige um retorno 200 OK rápido para confirmar o recebimento
    return {"status": "success"}