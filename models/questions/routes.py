from pprint import pprint

from flask import Blueprint, request, jsonify

from models.questions.question import Question

app = Blueprint("questions", __name__)


@app.route("/questions/<theme>", methods=["GET"])
def get_questions_by_theme(theme: str):
    # TODO check if the theme exist
    return jsonify([question.render() for question in Question.select_questions_by_theme(theme)])


@app.route("/questions", methods=["POST"])
def create(value: str, theme: str):
    return Question.create_question(value, theme)


@app.route("/questions/question/<identifiant>", methods=["GET"])
def get_question_by_id(identifiant: int):
    return jsonify(Question.get_question_by_id(identifiant).render())


@app.route("/questions/delete/<question_id>", methods=["DELETE"])
def delete_question(question_id: int):
    return Question.delete_question_by_id(question_id)
