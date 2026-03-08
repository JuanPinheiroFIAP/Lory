from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)


def test_webhook_endpoint():
    response = client.post("/webhooks/whatsapp", json={"message": "teste"})
    assert response.status_code in [200, 400]
