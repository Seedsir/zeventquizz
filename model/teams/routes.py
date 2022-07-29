from flask import Blueprint, request

from model.teams.manager import TeamManager


app = Blueprint("teams", __name__)


team_manager = TeamManager()


@app.route("/teams", methods=["GET"])
def get_all():
    return team_manager.get_all()


@app.route("/teams", methods=["POST"])
def create_team():
    body = request.get_json()
    return team_manager.create(body)


@app.route("/teams/<team_id>", methods=["GET"])
def get_team(team_id):
    return team_manager.get(team_id)


@app.route("/teams/<team_id>", methods=["DELETE"])
def delete_team(team_id):
    return team_manager.delete(team_id)
