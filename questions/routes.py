import logging
from typing import Dict
from uuid import uuid4
from flask import Blueprint, request

questions_app = Blueprint("questions", __name__)

logger = logging.getLogger(__name__)


class ItemNotFoundException(Exception):
    pass


class MemoryStorage:
    def __init__(self):
        self._storage = {}

    def get_id(self):
        return str(uuid4())

    def add(self, obj: Dict):
        obj["id"] = self.get_id()
        self._storage[obj["id"]] = obj
        return obj

    def get_all(self):
        return self._storage.values()

    def get(self, id: str):
        item = self._storage.get(id, None)
        if item is None:
            raise ItemNotFoundException
        return item

    def delete(self, id: str) -> None:
        del self._storage[id]


class QuestionsManager:
    def __init__(self) -> None:
        self._storage = MemoryStorage()

    def get_all_questions(self):
        return self._storage.get_all()

    def add(self, question: Dict) -> Dict:
        return self._storage.add(question)

    def get(self, question_id: str) -> Dict:
        question = {}
        try:
            question = self._storage.get(question_id)
        except ItemNotFoundException as inf:
            logger.warning(f"item {question_id} not found")
        finally:
            return question

    def delete(self, question_id: str) -> Dict:
        question = self.get(question_id)
        if not question:
            return question

        self._storage.delete(question_id)
        return question


question_manager = QuestionsManager()


@questions_app.route("/questions", methods=["GET"])
def get_all():
    questions = question_manager.get_all_questions()
    return [question for question in questions]


@questions_app.route("/questions", methods=["POST"])
def create():
    # TODO: Add check content of the body
    body = request.get_json()
    return question_manager.add(body)


@questions_app.route("/questions/<question_id>", methods=["GET"])
def get_question(question_id):
    question = question_manager.get(question_id)
    return question


@questions_app.route("/questions/<question_id>", methods=["DELETE"])
def delete_question(question_id):
    question = question_manager.delete(question_id)
    return question
