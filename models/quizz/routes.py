from flask import Blueprint, jsonify, Response, request

from models import Quizz
from flask_cors import CORS

app = Blueprint("quizz_app", __name__)
CORS(app)


@app.route("/quizz", methods=["POST"])
def create_quizz() -> Response:
    theme = str(request.data['theme'])
    nb_questions = int(request.data['nb_questions'])
    return jsonify([Quizz.create_quizz(theme, nb_questions).render()])


@app.route("/quizz/<quizz_id>", methods=["DELETE"])
def delete_quizz_by_id(quizz_id: int) -> Response:
    Quizz.delete_quizz(quizz_id)
    return jsonify([{
        "status": 200,
        "message": "Le Quizz a bien été supprimé."
    }])


@app.route("/quizz/<quizz_id>", methods=["GET"])
def get_quizz_by_id(quizz_id: int) -> Response:
    return jsonify([Quizz.get_quizz(quizz_id).render()])


@app.route("/quizz/<quizz_id>/questions", methods=["GET"])
def get_question_quizz(quizz_id: int) -> Response:
    return jsonify([question.render() for question in Quizz.get_questions_quizz(quizz_id)])
