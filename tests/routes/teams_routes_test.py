from flask import url_for

from models import BattleQuizz
from models.scores.score import Score
from models.db import db


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


def test_get_team_score(client, battle):
    register_battle_id_in_db(battle)
    url = url_for('teams.get_team_score', battle_id=battle.id, team_id=battle.teams[0].id)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_update_team_score(client, battle):
    register_battle_id_in_db(battle)
    url = url_for('teams.update_team_score', battle_id=battle.id, team_id=battle.teams[0].id, point=7)
    response = client.put(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_delete_team(client, team):
    url = url_for('teams.delete_team', team_id=team.id)
    response = client.delete(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_add_player(client, app, user, team):
    url = url_for('teams.add_player', team_id=team.id, user_id=user.id)
    response = client.put(url)
    assert response.status_code == 200
    assert type(response.json) == list


def register_battle_id_in_db(battle: BattleQuizz) -> None:
    for team in battle.teams:
        score = db.session.query(Score).filter_by(id=team.score[0].id).first()
        score.battle_id = battle.id
        db.session.add(score)
        db.session.commit()
