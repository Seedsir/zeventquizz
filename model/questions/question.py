from model.db import db


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String())
    theme = db.Column(db.String())
    quizz_id = db.Column(db.Integer, db.ForeignKey('quizz.id'),
                         nullable=True)
    answers = db.relationship('Answer', backref='question', lazy=False)

    def render(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def select_questions_by_theme(theme: str) -> list['Question']:
        questions = Question.query.filter_by(theme=theme).all()
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
        return question
