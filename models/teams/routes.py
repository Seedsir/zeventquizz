from flask import Blueprint, jsonify

from models import Team

app = Blueprint("teams", __name__)


@app.route("/teams/team/add_player", methods=["POST"]) # TODO A revoir
def add_player():
    Team.add_player_to_team(3, 1)
    return {"status": "OK", "Message": f"Utilisateur 1 bien ajouté"}


@app.route("/teams/create/<streamer>", methods=["POST"])  # TODO Ne marche pas: Ajouter le streamer dans le body
def create_team(streamer: str):
    return Team.create_team(streamer)


@app.route("/teams/<team_id>", methods=["GET"])  # Fonctionne
def get_team(team_id: int):
    return jsonify(Team.get_team_by_id(team_id).render())


@app.route("/teams/<team_id>", methods=["DELETE"])  # Pas encore testé
def delete_team(team_id: int):
    return Team.delete_team_by_id(team_id)


@app.route("/teams/<team_id>/score", methods=["GET"])  # Fonctionne mais mal pensé
def get_team_score(team_id: int):
    return jsonify(Team.get_score(team_id))


@app.route("/teams/<team_id>/<point>", methods=["PUT"])  # Ne peux pas fonctionner car score non instancié
def update_team_score(team_id: int, point: int):
    return Team.get_update_scorescore(team_id, point)
