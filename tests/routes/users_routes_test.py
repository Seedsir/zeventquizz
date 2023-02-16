from flask import url_for


def test_get_user(client, user):
    url = url_for('users.get_user', username=user.username)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_get_user_by_id_twitch(client, user):
    url = url_for('users.get_user_by_id_twitch', id_twitch=user.id_twitch)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_delete_user(client, user):
    url = url_for('users.delete_user', user_id=user.id)
    response = client.delete(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_get_profile_with_token(client, user):
    url = url_for('users.get_profile')
    headers = {
        "token": "123123456"
    }
    response = client.get(url, headers=headers)
    assert response.request.headers.environ['HTTP_TOKEN'] == headers['token']
    assert type(response.json) == list
    assert response.json[0]['status_code'] == 401

def test_get_profile_without_token(client, user):
    url = url_for('users.get_profile')
    headers = {}
    response = client.get(url, headers=headers)
    assert response.request.headers.environ.get('HTTP_TOKEN') is None
    assert response.json is None
    assert response.status_code == 403
