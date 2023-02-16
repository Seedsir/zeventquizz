from flask import url_for


def test_get_questions_by_theme(client, question):
    url = url_for('questions.get_questions_by_theme', theme=question.theme)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_create_question(client):
    url = url_for('questions.create_question')
    data = {
        "value": "Cette question est-elle bien enregistrée ?",
        "theme": "Création de question",
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert type(response.json) == list


def test_get_question_by_id(client, question):
    url = url_for('questions.get_question_by_id', question_id=question.id)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_delete_question(client, question):
    url = url_for('questions.delete_question', question_id=question.id)
    response = client.delete(url)
    assert response.status_code == 200
    assert type(response.json) == list
