from flask import Blueprint, jsonify

from model import Answer

app = Blueprint("answers", __name__)


@app.route("/answers/<question_id>", methods=["GET"])
def get_all_possible_answers(question_id: int):
    return Answer.get_all_possible_answers(question_id)


@app.route("/answers/<question_id>/answer", methods=["GET"])
def get_good_answer(question_id: int):
    return jsonify(Answer.get_good_answer(question_id).render())


@app.route("/answers/<question_id>", methods=["POST"])
def create_answer(question_id: int, value: str, is_true: bool):
    return Answer.create_answer(question_id, value, is_true)


@app.route("/answers/<answer_id>", methods=["DELETE"])
def delete_answer(answer_id: int):
    return Answer.delete_answer_by_id(answer_id)
