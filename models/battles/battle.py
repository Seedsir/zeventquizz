from typing import List

from models.db import db
from models.quizz.quizz import Quizz
import uuid
from models.teams.team import Team


class BattleQuizz(db.Model):
    __tablename__ = "battles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    theme = db.Column(db.String())
    stremers_number = db.Column(db.Integer())
    questions_number = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=True)
    is_active = db.Column(db.Boolean(), nullable=False, default=False)
    teams = db.relationship('Team', backref='battlequizz', lazy=False)
    quizz = db.relationship('Quizz', backref='battlequizz', lazy=False)

    def __init__(self, name: str, streamers_list: list, theme: str, questions_number: int):
        self.name = name
        self.streamer_list = streamers_list
        self.theme = theme
        self.questions_number = questions_number
        self.quizz = [Quizz(theme, questions_number)]
        self.teams = self.create_teams()

    @property
    def subscribe_url(self) -> str:
        # TODO encode the url with urllib
        token = uuid.uuid4()
        url = f"http://127.0.0.1:5000/battle/{self.theme}/{token}"
        return url

    def create_teams(self) -> List['Team']:
        for streamer in self.streamer_list:
            self.teams.append(Team(streamer))
            return self.teams

    def start_battle(self) -> None:
        self.is_active = True
        db.session.add(self)
        db.session.commit()

    def end_battle(self) -> None:
        self.is_active = False
        db.session.add(self)
        db.session.commit()

    def get_teams(self) -> List[Team]:
        return self.teams

    def __str__(self):
        return self.name

    def render(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def get_all_active_battles() -> list['BattleQuizz']:
        return BattleQuizz.query.filter_by(is_active=True).all()

    @staticmethod
    def create_battle(name: str, streamers: list, theme: str, questions_number: int) -> None:
        battle = BattleQuizz(name, streamers, theme, questions_number)
        battle.stremers_number = len(streamers)
        db.session.add(battle)
        db.session.commit()

    @staticmethod
    def get_battle_by_id(unique_id: int) -> 'BattleQuizz':
        battle = BattleQuizz.query.filter_by(id=unique_id).first()
        return battle

    @staticmethod
    def delete_battle_by(unique_id: int) -> None:
        battle = BattleQuizz.query.filter_by(id=unique_id).first()
        db.session.delete(battle)
        db.session.commit()
