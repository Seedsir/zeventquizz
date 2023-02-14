from flask import Blueprint, request

from models import User, Team
from models.battles.battle import BattleQuizz
from flask import jsonify

app = Blueprint("battles", __name__)


@app.route("/battles", methods=["POST"])
def create_battle():
    name = str(request.data['name'])
    streamers = list(request.data['streamers'])
    theme = str(request.data['theme'])
    question_number = int(request.data['question_number'])
    BattleQuizz.create_battle(name, streamers, theme, question_number)
    return jsonify([{"status": 200, "message": "Battle created"}])


@app.route("/battles", methods=["GET"])
def get_all_active_battles():
    return jsonify([battle.render() for battle in BattleQuizz.get_all_active_battles()])


@app.route("/battles/<battle_id>/subscribe_url", methods=["GET"])
def get_subscribe_url(battle_id: int):
    battle = BattleQuizz.get_battle_by_id(battle_id)
    return jsonify([{
        "battle_id": battle.id,
        "battle_name": battle.name,
        "subscribe_url": battle.subscribe_url,
    }])


@app.route("/battles/<battle_id>", methods=["GET"])
def get_battle(battle_id):
    return jsonify([BattleQuizz.get_battle_by_id(battle_id).render()])


@app.route("/battles/<battle_id>", methods=["DELETE"])
def delete_battle(battle_id):
    return BattleQuizz.delete_battle_by(battle_id)


@app.route("/battles/<battle_id>/teams", methods=["GET"])
def get_teams_battle(battle_id: int):
    battle = BattleQuizz.get_battle_by_id(battle_id)
    return jsonify([team.render() for team in battle.get_teams()])


@app.route("/battles/<battle_id>/<team_id>/<username>", methods=["PUT"])
def select_team(battle_id: int, team_id: int, username: str):
    User.select_a_team(username, team_id)
    return jsonify([{
        "status_code": 200,
        "message": f"{username} à bien rejoint l'équipe {team_id}"
    }])
