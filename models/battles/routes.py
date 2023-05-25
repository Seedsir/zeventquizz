from flask import Blueprint, request, Response, redirect

from models import User
from models.battles.battle import BattleQuizz
from flask import jsonify
from loguru import logger
app = Blueprint("battles", __name__)


@app.route("/battles/createBattle", methods=["POST"])
def create_battle() -> 'Response':
    logger.info("Je suis bien arrivé dans le fonction")
    name = str(request.form['name'])
    streamers = list(request.form['streamers'])
    theme = str(request.form['theme'])
    question_number = int(request.form['question_number'])
    BattleQuizz.create_battle(name, streamers, theme, question_number)
    return redirect(f'http://localhost:3000/startBattle')


@app.route("/battles", methods=["GET"])
def get_all_active_battles() -> 'Response':
    return jsonify([battle.render() for battle in BattleQuizz.get_all_active_battles()])


@app.route("/battles/<battle_id>/subscribe_url", methods=["GET"])
def get_subscribe_url(battle_id: int) -> 'Response':
    return jsonify([BattleQuizz.get_battle_by_id(battle_id).render()])


@app.route("/battles/<battle_id>", methods=["GET"])
def get_battle(battle_id: int) -> 'Response':
    return jsonify([BattleQuizz.get_battle_by_id(battle_id).render()])


@app.route("/battles/<battle_id>", methods=["DELETE"])
def delete_battle(battle_id: int) -> 'Response':
    BattleQuizz.delete_battle_by(battle_id)
    return jsonify([{
        "status": 200,
        "message": "Battle deleted"
    }])


@app.route("/battles/<battle_id>/teams", methods=["GET"])
def get_teams_battle(battle_id: int) -> 'Response':
    battle = BattleQuizz.get_battle_by_id(battle_id)
    return jsonify([team.render() for team in battle.get_teams()])


@app.route("/battles/<battle_id>/<team_id>/<username>", methods=["PUT"])
def select_team(battle_id: int, team_id: int, username: str) -> 'Response':
    User.select_a_team(username, team_id)
    return jsonify([{
        "status_code": 200,
        "message": f"{username} à bien rejoint l'équipe {team_id}"
    }])
