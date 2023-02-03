from flask import Blueprint, jsonify

from models import Team

app = Blueprint("teams", __name__)


@app.route("/teams", methods=["POST"])
def create_team(streamer: str):
    return Team.create_team(streamer)


@app.route("/teams/<team_id>", methods=["GET"])
def get_team(team_id: int):
    return jsonify(Team.get_team_by_id(team_id).render())


@app.route("/teams/<team_id>", methods=["DELETE"])
def delete_team(team_id: int):
    return Team.delete_team_by_id(team_id)


@app.route("/teams/<team_id>/<user_id>", methods=["PUT"])
def add_player(team_id: int, user_id: int):
    return Team.add_player_to_team(team_id, user_id)


@app.route("/teams/<team_id>/score", methods=["GET"])
def get_team_score(team_id: int):
    return Team.get_score(team_id)


@app.route("/teams/<team_id>/<point>", methods=["PUT"])
def update_team_score(team_id: int, point: int):
    return Team.get_update_scorescore(team_id, point)
