from app import app


def client():
    return app.test_client()


def test_index_returns_message_and_version():
    r = client().get("/")
    assert r.status_code == 200
    body = r.get_json()
    assert "message" in body
    assert "version" in body


def test_health_is_ok():
    r = client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_echo():
    r = client().get("/api/echo/hello")
    assert r.status_code == 200
    assert r.get_json() == {"echo": "hello", "length": 5}


def test_unknown_route_is_404():
    assert client().get("/nope").status_code == 404
