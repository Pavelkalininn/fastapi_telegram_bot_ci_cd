from fastapi.testclient import TestClient
from main import BREAD, CAT, HELP, IS_HAVE_EARS, NOT_UNDERSTAND, app

client = TestClient(app)
TEST_USER = 33344455566


def test_send_message():
    response = client.get(f'/{TEST_USER}/start/')
    assert response.status_code == 200
    assert response.json() == HELP
    response = client.get(f'/{TEST_USER}/дА/')
    assert response.json() == IS_HAVE_EARS
    response = client.get(f'/{TEST_USER}/НеТ/')
    assert response.json() == BREAD

    client.get(f'/{TEST_USER}/start/')
    response = client.get(f'/{TEST_USER}/дА/')
    assert response.json() == IS_HAVE_EARS
    response = client.get(f'/{TEST_USER}/ДА/')
    assert response.json() == CAT

    client.get(f'/{TEST_USER}/start/')
    response = client.get(f'/{TEST_USER}/НЕТ/')
    assert response.json() == CAT


def test_send_wrong_text():
    response = client.get(f'/{TEST_USER}/test_text/')
    assert response.status_code == 200
    assert response.json() == NOT_UNDERSTAND


def test_bad_telegram_id():
    response = client.get("/test_text/test_text/").json()
    assert len(response) == 2
    assert response[1] == 400
    assert response[0] == {'status': 'Bad Request'}
