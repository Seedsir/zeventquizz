import random

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


def test_get_all_active_battles(client):
    url = url_for('battles.get_all_active_battles')
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_get_subscribe_url(client, battle):
    url = url_for('battles.get_subscribe_url', battle_id=battle.id)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_get_battle(client, battle):
    url = url_for('battles.get_battle', battle_id=battle.id)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_get_teams_battle(client, battle):
    url = url_for('battles.get_teams_battle', battle_id=battle.id)
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json) == list


def test_select_team(client, battle, user):
    index = random.randint(0, len(battle.teams)-1)
    team_id = battle.teams[index].id
    url = url_for('battles.select_team',
                  battle_id=battle.id,
                  team_id=team_id,
                  username=user.username)
    response = client.put(url)
    assert response.status_code == 200
    assert type(response.json) == list
