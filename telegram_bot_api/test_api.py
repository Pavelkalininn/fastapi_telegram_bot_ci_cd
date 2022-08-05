from fastapi.testclient import TestClient
from main import app, BREAD, IS_HAVE_EARS, HELP, NOT_UNDERSTAND


client = TestClient(app)
test_user = 33344455566


def test_send_message():
    response = client.get(f'/{test_user}/start/')
    assert response.status_code == 200
    assert response.json() == HELP
    second_response = client.get(f'/{test_user}/дА/')
    assert second_response.json() == IS_HAVE_EARS
    third_response = client.get(f'/{test_user}/НеТ/')
    assert third_response.json() == BREAD


def test_send_wrong_text():
    response = client.get(f'/{test_user}/test_text/')
    assert response.status_code == 200
    assert response.json() == NOT_UNDERSTAND


def test_bad_telegram_id():
    response = client.get("/test_text/test_text/").json()
    assert len(response) == 2
    assert response[1] == 400
    assert response[0] == {'status': 'Bad Request'}
