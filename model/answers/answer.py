import json

from model.db import db


class Answer(db.Model):
    __tablename__ = "answers"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String())
    is_true = db.Column(db.Boolean())
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'),
                            nullable=False)

    def __init__(self, question_id: int, value: str, is_true: bool):
        self.question_id = question_id
        self.value = value
        self.is_true = is_true

    def render(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __str__(self):
        return self.value

    @staticmethod
    def get_all_possible_answers(identifiant: int) -> list['Answer']:
        answers = Answer.query.filter_by(question_id=identifiant).all()
        db.session.commit()
        return answers

    @staticmethod
    def get_good_answer(identifiant: int) -> 'Answer':
        answers = Answer.query.filter_by(question_id=identifiant).all()
        db.session.commit()
        answer = [answer for answer in answers if answer['is_true'] is True]
        return answer[0]

    @staticmethod
    def create_answer(question_id: int, value: str, is_true: bool) -> None:
        answer = Answer(question_id, value=value, is_true=is_true)
        db.session.add(answer)
        db.session.commit()

    @staticmethod
    def delete_answer_by_id(identifiant: int) -> None:
        question = Answer.query.filter_by(id=identifiant).first()
        db.session.delete(question)
        db.session.commit()