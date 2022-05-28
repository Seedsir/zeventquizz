from typing import Dict
from uuid import uuid4
from flask import Blueprint, request

from questions.manager import QuestionsManager

app = Blueprint("questions", __name__)

question_manager = QuestionsManager()


@app.route("/questions", methods=["GET"])
def get_all():
    questions = question_manager.get_all()
    return [question for question in questions]


@app.route("/questions", methods=["POST"])
def create():
    # TODO: Add check content of the body
    body = request.get_json()
    return question_manager.create(body)


@app.route("/questions/<question_id>", methods=["GET"])
def get_question(question_id):
    question = question_manager.get(question_id)
    return question


@app.route("/questions/<question_id>", methods=["DELETE"])
def delete_question(question_id):
    question = question_manager.delete(question_id)
    return question
