from flask import url_for


def test_add_player(client, app, user):
    url = url_for('teams.add_player')
    response = client.post(url)
    assert response.status_code == 200
    assert response.json == {"status": "OK", "Message": f"Utilisateur 1 bien ajouté"}