from app.core.config import settings

def test_token_login_success(client):
    r = client.post(f"{settings.API_V1_STR}/auth/token", data={"username": "demo@example.com", "password": "demo123"})
    assert r.status_code == 200
    body = r.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_token_login_failure(client):
    r = client.post(f"{settings.API_V1_STR}/auth/token", data={"username": "demo@example.com", "password": "wrong"})
    assert r.status_code == 401
