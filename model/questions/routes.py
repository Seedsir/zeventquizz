from flask import Blueprint, request, jsonify

from model.questions.question import Question

app = Blueprint("questions", __name__)


# @app.route("/questions", methods=["GET"])
# def get_all():
#     questions = question_manager.get_all()
#     return [question for question in questions]

@app.route("/questions/<theme>", methods=["GET"])
def get_questions_by_theme(theme: str):
    return jsonify([question.render() for question in Question.select_questions_by_theme(theme)])


@app.route("/questions", methods=["POST"])
def create(value: str, theme: str):
    return Question.create_question(value, theme)


@app.route("/questions/<question_id>", methods=["GET"])
def get_question_by_id(question_id: int):
    return jsonify(Question.get_question_by_id(question_id).render())


@app.route("/questions/<question_id>", methods=["DELETE"])
def delete_question(question_id: int):
    return Question.delete_question_by_id(question_id)


# @app.route("/questions/<question_id>/answers", methods=["GET"])
# def get_question_answers(question_id):
#     return question_manager.get_question_answers(question_id)
#
#
# @app.route("/questions/<question_id>/answers/<answer_id>", methods=["PUT"])
# def add_answer_to_questions(question_id, answer_id):
#     return question_manager.add_answer_to_question(question_id, answer_id)
