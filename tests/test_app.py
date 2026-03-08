from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)


def test_webhook_endpoint():
    payload = {
        "data": {
            "message": {"conversation": "teste"},
            "key": {"remoteJid": "5511999999999@s.whatsapp.net"},
        }
    }

    response = client.post("/webhooks/whatsapp", json=payload)

    assert response.status_code == 200
