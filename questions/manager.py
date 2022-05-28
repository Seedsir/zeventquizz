from storage import MemoryStorage
from typing import Dict
from exceptions import ItemNotFoundException
import logging

logger = logging.getLogger(__name__)


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
