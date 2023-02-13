from flask import url_for


def test_create_battle(client, question):
    url = url_for('battles.create_battle')
    data = {
        "name": "La team des Dingos du test",
        "streamers": ["Zeratroll", "Sixenus", "DFGood"],
        "theme": "Creation de battle",
        "question_number": 20,
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert type(response.json) == list
