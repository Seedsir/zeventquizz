from sqlalchemy.orm import joinedload

from models.db import db
from models.questions.question import Question
from loguru import logger
questions_of_quizz = db.Table('questions_of_quizz',
                       db.Column('quizz_id', db.Integer, db.ForeignKey('quizz.id'), primary_key=True),
                       db.Column('question_id', db.Integer, db.ForeignKey('questions.id'), primary_key=True)
                       )

class Quizz(db.Model):
    __tablename__ = "quizz"

    id = db.Column(db.Integer, primary_key=True)
    questions_number = db.Column(db.Integer())
    theme = db.Column(db.String())

    battle_id = db.Column(db.Integer, db.ForeignKey('battles.id'), nullable=True)
    questions = db.relationship('Question', secondary=questions_of_quizz, backref='questions')

    def __init__(self, theme: str, question_number: int):
        self.theme = theme
        self.questions_number = question_number
        self.questions = Question.select_questions_by_theme(self.theme, self.questions_number)
        # if question_number > len(self.questions):
        #     raise Exception(  # TODO create a correcte exception
        #         f"Limite maximale de questions dépassée, "
        #         f"merci de ne pas dépasser {len(self.questions)} sur le thème : {self.theme}")
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

    def __str__(self):
        return f"Quizz de la battle numéro {self.battle_id} - thème {self.battlequizz.theme}"

    @staticmethod
    def create_quizz(theme: str, nb_questions: int) -> 'Quizz':
        quizz = Quizz(theme, nb_questions)
        db.session.add(quizz)
        db.session.commit()
        return quizz

    @staticmethod
    def delete_quizz(identifiant: int) -> None:
        quizz = Quizz.query.filter_by(id=identifiant).first()
        db.session.delete(quizz)
        db.session.commit()

    @staticmethod
    def get_quizz(identifiant: int) -> 'Quizz':
        quizz = Quizz.query.get(identifiant)
        return quizz


    @staticmethod
    def get_questions_quizz(identifiant: int) -> ['Question']:
        questions = Question.query.join(questions_of_quizz).filter(questions_of_quizz.c.quizz_id == identifiant).all()
        logger.info(f"Identifiant={identifiant}, Je recherche mes questions s'il vous plait: {questions}")
        return questions
