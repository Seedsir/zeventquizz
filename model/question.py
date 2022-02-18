from model.response import Response


class Question:

    def __init__(self, question_id):
        self.id = question_id
        self.answers = Response(self.id).get_possible_answers()