from flask import Blueprint, request

from models import User, Team
from models.battles.battle import BattleQuizz
from flask import jsonify

app = Blueprint("battles", __name__)


@app.route("/battles", methods=["POST"])
def create_battle(name: str, streamers: list, theme: str, question_number: int):
    return BattleQuizz.create_battle(name, streamers, theme, question_number)


@app.route("/battles", methods=["GET"])
def get_all():
    return jsonify([battle.render() for battle in BattleQuizz.get_all_battles()])


@app.route("/battles", methods=["GET"])
def get_suscribe_url():
    return jsonify([battle.render() for battle in BattleQuizz.get_all_battles()])


@app.route("/battles/<battle_id>", methods=["GET"])
def get_battle(battle_id):
    return jsonify(BattleQuizz.get_battle_by_id(battle_id).render())


@app.route("/battles/<battle_id>", methods=["DELETE"])
def delete_battle(battle_id):
    return BattleQuizz.delete_battle_by(battle_id)


@app.route("/battles/<battle_id>/teams", methods=["GET"])
def get_teams_battle(battle_id: int):
    return jsonify([team.render() for team in Team.get_teams(battle_id)])


@app.route("/battles/<battle_id>/<team_name>/<username>", methods=["POST"])
def select_team(battle_id: int, team_name: str, username: str):
    return User.select_a_team(username, battle_id, team_name)
