import pytest
from freezegun import freeze_time

from Amazon_killer import amazon_killer as app
from test_data import good_response, user_updated, \
    json_Ilia, bad_response, \
    json_create_user, json_cart, json_cart_put


@pytest.fixture
def store_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


@freeze_time('2021-02-08 14:16:41')
def test_create_user(store_app):
    response = store_app.post(
        '/users/create_user',
        json=json_Ilia)
    assert response.status_code == 201
    assert response.json == json_create_user
    user_id = response.json['user_id']
    response = store_app.get(f'/users/get_user/{user_id}')

    assert response.status_code == 200
    assert response.json == {
        "name": "Ilia",
        "email": "illia.sukonnik@gmail.com",
        "user_id": user_id,
        "registration_timestamp": '2021-02-08T14:16:41',
    }


def test_get_user_no_such_user(store_app):
    response = store_app.get('/users/get_user/0')

    assert response.status_code == 404
    assert response.json == bad_response


def test_put_user(store_app):
    response = store_app.put("/users/put_user/1", json=user_updated)
    assert response.status_code == 200
    assert response.json == good_response


def test_delete_user(store_app):
    response = store_app.delete("/users/delete_users/1")
    assert response.status_code == 200
    assert response.json == good_response


@freeze_time('2021-02-08 14:16:41')
def test_create_cart(store_app):
    response = store_app.post('/cart', json=json_cart)
    assert response.status_code == 201
    assert response.json == json_create_user
    user_id = response.json['user_id']
    response = store_app.get(f'/cart/{user_id}')

    assert response.status_code == 200
    assert response.json == {'registration_timestamp': '2021-02-08T14:16:41', 'user_id': 1}


def test_get_user_no_such_cart(store_app):
    response = store_app.get('/cart/0')

    assert response.status_code == 404
    assert response.json == {'error': 'no such user '}


def test_put_cart(store_app):
    response = store_app.put("/cart/1", json=json_cart_put)
    assert response.status_code == 200
    assert response.json == good_response


def test_delete_cart(store_app):
    response = store_app.delete("/cart/1")
    assert response.status_code == 200
    assert response.json == good_response
