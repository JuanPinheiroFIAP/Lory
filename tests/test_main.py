from fastapi.testclient import TestClient
from src.app.main import app


def test_app_lifespan():
    # O bloco 'with' dispara o @asynccontextmanager lifespan
    with TestClient(app) as client:
        response = client.get("/webhooks/whatsapp")  # Testa se as rotas carregaram
        # Mesmo que dê 405 (Method Not Allowed) porque é POST,
        # o lifespan já terá sido executado e coberto.
        assert response.status_code != 404
