from flask import Blueprint, request

from answers.manager import AnswerManager


app = Blueprint("answers", __name__)


answer_manager = AnswerManager()


@app.route("/answers", methods=["GET"])
def get_all():
    return answer_manager.get_all()


@app.route("/answer", methods=["POST"])
def create_answer():
    body = request.get_json()
    return answer_manager.create(body)


@app.route("/answers/<answer_id>", methods=["GET"])
def get_answer(answer_id):
    return answer_manager.get(answer_id)


@app.route("/answers/<answer_id>", methods=["DELETE"])
def delete_answer(answer_id):
    return answer_manager.delete(answer_id)
