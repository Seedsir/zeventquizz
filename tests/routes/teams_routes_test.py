from flask import url_for


def test_create_team(client, app, user):
    url = url_for('teams.create_team')
    data = {
        "streamer": user.username
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert type(response.json) == list


def test_get_team(client, team):
    url = url_for('teams.get_team', team_id=team.id)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_get_team_score(client, team): # TODO valeur en dure
    url = url_for('teams.get_team_score', battle_id=8, team_id=team.id)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_update_team_score(client, team): # TODO attention aux valeurs en dures
    url = url_for('teams.update_team_score', battle_id=8, team_id=23, point=7)
    response = client.put(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_delete_team(client, team):
    url = url_for('teams.delete_team', team_id=team.id)
    response = client.delete(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_add_player(client, app, user): # TODO c'est pas parce que ca marche que c'est bien.
    url = url_for('teams.add_player')
    response = client.post(url)
    assert response.status_code == 200
    assert response.json == {"status": "OK", "Message": f"Utilisateur 1 bien ajouté"}
