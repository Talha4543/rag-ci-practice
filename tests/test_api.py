from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_chunk_endpoint():
    r = client.post("/chunk", json={"text": "abcdefghij", "chunk_size": 5, "overlap": 0})
    assert r.status_code == 200
    assert r.json()["count"] == 2
