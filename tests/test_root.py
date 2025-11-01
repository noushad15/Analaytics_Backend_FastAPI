def test_root_endpoint(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "Welcome" in r.json().get("message", "")

