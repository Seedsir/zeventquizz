from flask import Blueprint, jsonify, request, Response

from models import Answer

app = Blueprint("answers", __name__)


@app.route("/answers/<question_id>", methods=["GET"])
def get_all_possible_answers(question_id: int) -> 'Response':
    return jsonify([answser.render() for answser in Answer.get_all_possible_answers(question_id)])


@app.route("/answers/<question_id>/answer", methods=["GET"])
def get_good_answer(question_id: int) -> 'Response':
    list_answer = []
    true_answer = [answer for answer in Answer.get_good_answer(question_id)][0].render()
    list_answer.append(true_answer)
    return jsonify(list_answer)


@app.route("/answers", methods=["POST"])
def create_answer() -> 'Response':
    question_id = int(request.data['question_id'])
    value = str(request.data['value'])
    is_true = eval(request.data['is_true'])
    Answer.create_answer(question_id, value, is_true)
    return jsonify([{"status": 200, "message": "Answer created"}])


@app.route("/answers/delete/<answer_id>", methods=["DELETE"])
def delete_answer(answer_id: int) -> 'Response':
    Answer.delete_answer_by_id(answer_id)
    return jsonify([{"status": 200, "message": "Answer deleted"}])
