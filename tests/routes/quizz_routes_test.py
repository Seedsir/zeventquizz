from flask import url_for


def test_get_quizz_by_id(client, battle):
    url = url_for('quizz_app.get_quizz_by_id', quizz_id=battle.quizz[0].id)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_create_quizz(client):
    url = url_for('quizz_app.create_quizz')
    data = {
        "theme": "Quizz random",
        "nb_questions": 7,
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert type(response.json) == list


def test_delete_quizz_by_id(client, battle):
    url = url_for('quizz_app.delete_quizz_by_id', quizz_id=battle.quizz[0].id)
    response = client.delete(url)
    assert response.status_code == 200
    assert type(response.json) == list
