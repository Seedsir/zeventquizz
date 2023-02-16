from flask import url_for


def test_get_all_possible_answers(client):
    url = url_for('answers.get_all_possible_answers', question_id=50)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_get_good_answer(client, question_with_true_answer):
    url = url_for('answers.get_good_answer', question_id=question_with_true_answer.id)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_create_answer(client, question):
    url = url_for('answers.create_answer')
    data = {
        "question_id": question.id,
        "value": "Test d'insertion de réponse",
        "is_true": False,
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert type(response.json) == list


def test_delete_answer(client, answer):
    url = url_for('answers.delete_answer', answer_id=answer.id)
    response = client.delete(url)
    assert response.status_code == 200
    assert type(response.json) == list
