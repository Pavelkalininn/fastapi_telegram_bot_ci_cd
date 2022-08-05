from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_send_message():
    response = client.get('/33444555/test_text/')
    assert response.status_code == 200
    assert response.json().get('telegram_id') == 33444555
    assert response.json().get('text') == 'test_text'


def test_bad_telegram_id():
    response = client.get("/test_text/test_text/").json()
    assert len(response) == 2
    assert response[1] == 400
    assert response[0] == {'status': 'Bad Request'}
