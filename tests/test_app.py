from flask.testing import FlaskClient


def test_index_returns_200(client: FlaskClient) -> None:
    res = client.get('/')
    assert res.status_code == 200


def test_login_returns_200(client: FlaskClient) -> None:
    res = client.get('/login')
    assert res.status_code == 200


def test_register_returns_200(client: FlaskClient) -> None:
    res = client.get('/register')
    assert res.status_code == 200


def test_reset_returns_200(client: FlaskClient) -> None:
    res = client.get('/reset')
    assert res.status_code == 200


def test_update_returns_200(client: FlaskClient) -> None:
    res = client.get('/update')
    assert res.status_code == 200
