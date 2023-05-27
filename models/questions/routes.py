from flask import Blueprint, request, jsonify, Response

from models.questions.question import Question

app = Blueprint("questions", __name__)


@app.route("/questions/<theme>", methods=["GET"])
def get_questions_by_theme(theme: str, question_number: int) -> 'Response':
    # TODO check if the theme exist
    return jsonify([question.render() for question in Question.select_questions_by_theme(theme, question_number)])


@app.route("/questions", methods=["POST"])
def create_question() -> 'Response':
    value = str(request.data['value'])
    theme = str(request.data['theme'])
    Question.create_question(value, theme)
    return jsonify([{
        "status": 200,
        "message": "Question created"
    }])


@app.route("/questions/question/<question_id>", methods=["GET"])
def get_question_by_id(question_id: int) -> 'Response':
    return jsonify([Question.get_question_by_id(question_id).render()])


@app.route("/questions/delete/<question_id>", methods=["DELETE"])
def delete_question(question_id: int) -> 'Response':
    Question.delete_question_by_id(question_id)
    return jsonify([{
        "status": 200,
        "message": "Question deleted"
    }])
