"""File to test API endpoints."""
from fastapi.testclient import TestClient
import pytest
from api.main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"result": "Welcome to the NLP API"}


def test_process():
    """Test normal processing."""
    response = client.post('/process', json={"text": "This is a test"})
    assert response.status_code == 200
    assert response.json() == {
        'noun_phrases': ['This', 'a test']
    }


# Still can't get this to work without celery looking for an amqp broker
# def test_delayed_process(celery_worker):
#     """Test celery processing."""
#     response = client.post('/delayed_process', json={"text": "This is a test"})
#     assert response.status_code == 200
#     assert response.json() == {
#         'noun_phrases': ['This', 'a test']
#     }

