from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)


def test_webhook_message_upsert():
    payload = {
        "event": "MESSAGES_UPSERT",  # Isso faz o código entrar na linha 12
        "data": {
            "message": {"conversation": "Teste de gasto Lory"},
            "key": {"remoteJid": "5511999999999@s.whatsapp.net"},
        },
    }
    response = client.post("/webhooks/whatsapp", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
