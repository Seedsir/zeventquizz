from loguru import logger
from models.db import db
from models.questions.exceptions import OuyOfNumberException


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String())
    theme = db.Column(db.String())
    point = db.Column(db.Integer, nullable=True)
    difficulty = db.Column(db.String(), nullable=True)
    quizz_id = db.Column(db.Integer, db.ForeignKey('quizz.id'),
                         nullable=True)
    answers = db.relationship('Answer', backref='question', lazy=False)

    def render(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __str__(self):
        return self.value

    @staticmethod
    def select_questions_by_theme(theme: str, question_number: int) -> list['Question']:
        total_questions = Question.query.filter_by(theme=theme).all()
        if question_number > len(total_questions):
            logger.error(f"Le nombre de questions désiré est trop grand, max {len(total_questions)}")
            raise OuyOfNumberException()
        elif question_number == len(total_questions):
            return total_questions
        else:
            questions = Question.query.filter_by(theme=theme).limit(question_number).all()
            return questions

    @staticmethod
    def create_question(value: str, theme: str) -> None:
        question = Question(value=value, theme=theme)
        db.session.add(question)
        db.session.commit()

    @staticmethod
    def delete_question_by_id(identifiant: int) -> None:
        question = Question.query.filter_by(id=identifiant).first()
        db.session.delete(question)
        db.session.commit()

    @staticmethod
    def get_question_by_id(identifiant: int)-> 'Question':
        question = Question.query.filter_by(id=identifiant).first()
        db.session.commit()
        return question
