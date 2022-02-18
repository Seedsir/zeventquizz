class Response:

    def __init__(self, question_id):
        self.question_id = question_id

    def get_possible_answers(self):
        return[ x for x in ANSWER_DICT['answer'] if ANSWER_DICT['id'] == self.question_id]