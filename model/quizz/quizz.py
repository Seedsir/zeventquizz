from model.db import db
from model.questions.question import Question


class Quizz(db.Model):
    __tablename__ = "quizz"

    id = db.Column(db.Integer, primary_key=True)
    questions_number = db.Column(db.Integer())
    theme = db.Column(db.String())
    battle_id = db.Column(db.Integer, db.ForeignKey('battles.id'), nullable=False)
    questions = db.relationship('Question', backref='quizz', lazy=True)

    def __init__(self, theme: str, question_number: int):
        self.theme = theme.lower()
        self.question_number = question_number  # TODO reflechir au fait que ca ne sert a rien de le garder dans l'objet
        self.questions = Question.select_questions_by_theme(question_number, theme)
        if question_number > len(self.questions):
            raise Exception(  # TODO create a correcte exception
                f"Limite maximale de questions dépassée, "
                f"merci de ne pas dépasser {len(self.questions)} sur le thème : {self.theme}")
        self.progress = None

    def quizz_progress(self, index: int):
        progress = index / self.question_number * 100
        self.progress = int(progress)
        return self.progress

    def read_quizz(self):
        for question in self.questions:
            question.get_answers()

    def render(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def create_quizz(theme: str, nb_questions: int) -> 'Quizz':
        quizz = Quizz(theme, nb_questions)
        db.session.add(quizz)
        db.session.commit()
        return quizz

    @staticmethod
    def delete_quizz(identifiant: int) -> None:
        quizz = Quizz.query.filter(id=identifiant).first()
        db.session.delete(quizz)
        db.session.commit()

    @staticmethod
    def get_quizz(identifiant: int) -> 'Quizz':
        return Quizz.query.filter(id=identifiant).first()
