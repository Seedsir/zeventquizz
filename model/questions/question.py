import random

from model.answers.response import Response


class Question:

    def __init__(self):
        self.id = None
        self.value = None
        self.answers = []

    def select_question(self, question_list: list):
        self.index = random.randint(0, len(question_list) - 1)
        self.id = question_list[self.index]["id"]
        self.value = question_list[self.index]["value"]

    def get_answers(self, answers_list: list):
        self.answers = Response(self.id).get_possible_answers(answers_list)


