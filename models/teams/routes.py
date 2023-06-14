from typing import List, Dict
from loguru import logger
from flask import Blueprint, jsonify, request, Response, redirect

from models import Team

app = Blueprint("teams", __name__)


@app.route("/teams/<team_id>/<username>", methods=["PUT"])
def add_player(team_id: int, username: str) -> 'Response':
    Team.add_player_to_team(username, int(team_id))
    logger.info(f"User: {username} correctly added in the team id: {team_id}")
    return jsonify([{
        "status_code": 200,
        "message": f"User: {username} correctly added in the team id: {team_id}",
    }])


@app.route("/teams/create", methods=["POST"])
def create_team() -> 'Response':
    streamer = str(request.data['streamer'])
    Team.create_team(streamer)
    return jsonify([{
        "status": "OK",
        "message": f"L'équipe de {streamer} à bien été créée",
    }])


@app.route("/teams/<team_id>", methods=["GET"])
def get_team(team_id: int) -> 'Response':
    return jsonify([Team.get_team_by_id(team_id).render()])


@app.route("/teams/<team_id>", methods=["DELETE"])
def delete_team(team_id: int) -> 'Response':
    Team.delete_team_by_id(team_id)
    return jsonify([{
        "status": "OK",
        "message": f"L'équipe id: {team_id} a bien été supprimée."
    }])


@app.route("/<battle_id>/teams/<team_id>/score", methods=["GET"])
def get_team_score(battle_id: int, team_id: int) -> 'Response':
    return jsonify([Team.get_score(team_id, battle_id=battle_id).render()])


@app.route("/<battle_id>/teams/<team_id>/<point>", methods=["PUT"])
def update_team_score(battle_id: int, team_id: int, point: int) -> 'Response':
    Team.update_score(battle_id, team_id, point)
    return jsonify([{
        "status": "OK",
        "message": f"Le score de l'équipe: {team_id} a bien été mis a jour."
    }])
