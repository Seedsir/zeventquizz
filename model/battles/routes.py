from flask import Blueprint, request
from model.battles.battle import BattleQuizz
from flask import jsonify
app = Blueprint("battles", __name__)

@app.route("/battles", methods=["GET"])
def get_all():
    return jsonify([battle.render() for battle in BattleQuizz.get_all_battles()])

# @app.route("/battles/<battle_id>", methods=["GET"])
# def get_battle(battle_id):
#     return battle_manager.get(battle_id)
#
# @app.route("/battles/<battle_id>", methods=["DELETE"])
# def delete_battle(battle_id):
#     return battle_manager.delete(battle_id)
#
# @app.route("/battles", methods=["POST"])
# def create():
#     # TODO: Add check content of the body
#     body = request.get_json()
#     return battle_manager.create(body)