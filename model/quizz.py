import json

from model.question import Question


class Quizz:

    def __init__(self, theme: str, question_number: int):
        self.theme = theme.lower()
        self.question_number = question_number
        self.questions = []

    def create_quizz(self):
        with open(r"E:\zeventquizz\utils\theme\{}\questions.json".format(self.theme), "r") as questions:
            data_questions = json.load(questions)

        with open(r"E:\zeventquizz\utils\theme\{}\answers.json".format(self.theme), "r") as answers:
            data_answers = json.load(answers)

        for i in range(self.question_number):
            question = Question()
            question.select_question(data_questions)
            question.get_answers(data_answers)
            self.questions.append(question)
            data_questions.pop(question.index)



if __name__ == '__main__':
    u = Quizz("Zevent", 3)
    u.create_quizz()
    print(u.questions)
