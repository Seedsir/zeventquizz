import re

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
    streamers = re.findall(r"(\w+)", request.form['streamers'])
    theme = str(request.form['theme'])
    question_number = int(request.form['question_number'])
    BattleQuizz.create_battle(name, streamers, theme, question_number)
    return redirect(f'http://localhost:3000/startBattle')


@app.route("/battles", methods=["GET"])
def get_all_created_battles() -> 'Response':
    return jsonify([battle.render() for battle in BattleQuizz.get_all_created_battles()])


@app.route("/battles/active_battle/<battle_id>", methods=['PUT'])
def active_battle(battle_id: str) -> 'Response':
    #logger.info(request.headers.get('Token'))
    # TODO faire le check sur l'access token
    if battle_id is None:
        raise Exception()
    BattleQuizz.start_battle(int(battle_id))
    return jsonify([{
        "code": 200,
        "message": f"La battle {battle_id} est correctement activée",
    }])


@app.route("/battles/deactive_battle/<battle_id>", methods=['PUT'])
def deactive_battle(battle_id: str) -> 'Response':
    # logger.info(request.headers.get('Token'))
    # TODO faire le check sur l'access token
    if battle_id is None:
        raise Exception()
    BattleQuizz.end_battle(int(battle_id))
    return jsonify([{
        "code": 200,
        "message": f"La battle {battle_id} est correctement activée",
    }])


@app.route("/battles/<battle_id>/subscribe_url", methods=["GET"])
def get_subscribe_url(battle_id: int) -> 'Response':
    return jsonify([BattleQuizz.get_battle_by_id(battle_id).render()])


@app.route("/battles/<battle_id>", methods=["GET"])
def get_battle(battle_id: int) -> 'Response':
    return jsonify([BattleQuizz.get_battle_by_id(battle_id).render()])


@app.route("/battles/name/<battle_name>", methods=["GET"])
def get_battle_by_name(battle_name: str) -> 'Response':
    return jsonify([BattleQuizz.get_battle_by_name(battle_name).render()])


@app.route("/battles/<battle_id>", methods=["DELETE"])
def delete_battle(battle_id: int) -> 'Response':
    BattleQuizz.delete_battle_by(battle_id)
    return jsonify([{
        "status": 200,
        "message": "Battle deleted"
    }])


@app.route("/battles/<battle_id>/teams", methods=["GET"])
def get_teams_battle(battle_id: int) -> 'Response':
    teams = BattleQuizz.get_teams_of_battle(battle_id)
    return jsonify([team.render() for team in teams])



@app.route("/battles/<battle_id>/quizz_id", methods=["GET"])
def get_quizz_of_the_battle(battle_id: int) -> 'Response':
    return jsonify([BattleQuizz.get_the_quizz_of_the_battle(battle_id).render()])