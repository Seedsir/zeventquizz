from flask import Blueprint, jsonify

from models import Quizz

app = Blueprint("quizz_app", __name__)


@app.route("/quizz", methods=["POST"])
def create_quizz(theme: str, nb_questions: int):
    return jsonify(Quizz.create_quizz(theme, nb_questions).render())


@app.route("/quizz", methods=["DELETE"])
def delete_quizz_by_id(identifiant: int):
    return Quizz.delete_quizz(identifiant)


@app.route("/quizz/<identifiant>", methods=["GET"])
def get_quizz_by_id(identifiant: int):
    return jsonify(Quizz.get_quizz(identifiant).render())
