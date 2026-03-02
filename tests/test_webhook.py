import pytest
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_whatsapp_webhook_receive_message():
    # 1. Simula o JSON que a Meta enviaria
    payload = {
        "object": "whatsapp_business_account",
        "entry": [{
            "id": "12345",
            "changes": [{
                "value": {
                    "messages": [{
                        "from": "5511999999999",
                        "text": {"body": "Olá, Lory!"}
                    }]
                },
                "field": "messages"
            }]
        }]
    }

    # 2. Faz a requisição POST para a sua rota
    response = client.post("/webhooks/whatsapp", json=payload)

    # 3. Validações
    assert response.status_code == 200
    assert response.json() == {"status": "success"}