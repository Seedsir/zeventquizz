from model.db import db
from model.quizz.quizz import Quizz
import uuid
from model.teams.team import Team


class BattleQuizz(db.Model):
    __tablename__ = "battles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    stremers_number = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False, default=False)
    teams = db.relationship('Team', backref='battlequizz', lazy=False)
    quizz = db.relationship('Quizz', backref='battlequizz', lazy=False)

    def __init__(self, name: str, streamers_list: list, theme: str, question_number: int):
        self.name = name
        self.streamer_list = streamers_list
        self.theme = theme
        self.quizz = Quizz(theme, question_number)
        self.create_teams()

    @property
    def suscribe_url(self) -> str:
        token = uuid.uuid4()
        url = f"http://127.0.0.1:5000/battle/{self.theme}/{token}"
        return url

    def create_teams(self) -> None:
        for streamer in self.streamer_list:
            self.teams.append(Team(streamer))

    def start_battle(self) -> None:
        self.is_active = True
        db.session.add(self)
        db.session.commit()

    def end_battle(self) -> None:
        self.is_active = False
        db.session.add(self)
        db.session.commit()

    def get_teams(self) -> dict:
        if not len(self.teams) > 0:
            return "Aucune équipe n'a été crée pour le moment"
        dict_teams = {}
        for equipe in self.teams:
            dict_teams[f'Equipe {self.teams.index(equipe)}'] = equipe.streamer
        return dict_teams

    def __str__(self):
        return self.name

    def render(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def get_all_battles() -> list['BattleQuizz']:
        return BattleQuizz.query.filter_by(is_active=True).all()

    @staticmethod
    def create_battle(name: str, streamers: list, theme: str, question_number: int) -> None:
        battle = BattleQuizz(name, streamers, theme, question_number)
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
