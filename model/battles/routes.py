from flask import Blueprint, request

from model.battles.manager import BattlesManager

app = Blueprint("battles", __name__)

battle_manager = BattlesManager()

@app.route("/battles", methods=["GET"])
def get_all():
    return battle_manager.get_all()

@app.route("/battles/<battle_id>", methods=["GET"])
def get_battle(battle_id):
    return battle_manager.get(battle_id)

@app.route("/battles/<battle_id>", methods=["DELETE"])
def delete_battle(battle_id):
    return battle_manager.delete(battle_id)

@app.route("/battles", methods=["POST"])
def create():
    # TODO: Add check content of the body
    body = request.get_json()
    return battle_manager.create(body)