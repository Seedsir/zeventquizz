from flask import Blueprint, jsonify

from model import Team

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


@app.route("/teams/<team_id>/<user_id>", methods=["GET"])
def add_player(team_id: int, user_id: int):
    return Team.add_player_to_team(team_id, user_id)
