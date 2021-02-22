import requests
from fastapi.testclient import TestClient
from src.api import app, post_json

client = TestClient(app)

class MockResponse:
    def __init__(self):
        self.status_code = 200,
        self.body = {
            "width": 146,
            "height": 110
        }

    @staticmethod
    def json():
        return

def test_generate():
    response = client.get('/')
    assert response.status_code == 200

def test_generate_images(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "post", mock_post)
    result = post_json('/generate', {"width": 125, "height": 110})
    assert result.status_code == (200,)
    assert result.body == {"width": 146, "height": 110}

def test_generate_images_inexistent_body():
    response = client.post('/generate')
    assert response.status_code == 422