from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_analyze_ticket():
    payload = {
        "title": "API outage",
        "description": "Production API has failed and caused an outage",
        "severity": "critical"
    }

    response = client.post("/analyze", json=payload)

    assert response.status_code == 200
    assert response.json()["risk_score"] >= 70
