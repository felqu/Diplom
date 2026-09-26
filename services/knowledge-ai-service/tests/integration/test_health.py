from fastapi.testclient import TestClient

from knowledge_ai_service.main import app


def test_health() -> None:
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "knowledge-ai-service"}
