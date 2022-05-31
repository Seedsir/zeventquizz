from answers.routes import answer_manager
from core.manager import EntityManager
from storage.storage import MemoryStorage
from typing import Dict
import logging

logger = logging.getLogger(__name__)


class QuestionsManager(EntityManager):
    def get_question_answers(self, question_id):
        question = self.get(question_id)
        answers_id = question.get("answers", [])

        return [answer_manager.get(answer_id) for answer_id in answers_id]

    def add_answer_to_question(self, question_id, answer_id):
        question = self.get(question_id)
        if not question:
            return question

        answer = answer_manager.get(answer_id)
        if not answer:
            return answer

        question["answers"].append(answer_id)
        return self.update(question)
