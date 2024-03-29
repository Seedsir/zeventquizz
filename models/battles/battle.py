from typing import List
from urllib.parse import urlencode
from models.db import db
from models.quizz.quizz import Quizz
import uuid
from models.teams.team import Team
from loguru import logger


class BattleQuizz(db.Model):
    __tablename__ = "battles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    theme = db.Column(db.String())
    streamers_number = db.Column(db.Integer())
    questions_number = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=True)
    status = db.Column(db.String(), default="CREATED")
    teams = db.relationship('Team', backref='battlequizz', lazy=False)
    quizz = db.relationship('Quizz', backref='battlequizz', lazy=False)

    def __init__(self, name: str, streamers_list: list, theme: str, questions_number: int):
        self.name = name
        self.streamer_list = streamers_list
        self.theme = theme
        self.questions_number = questions_number
        self.quizz = [Quizz(self.theme, self.questions_number)]
        self.teams = self.create_teams()

    @property
    def subscribe_url(self) -> str:
        token = uuid.uuid4()
        url = f"http://127.0.0.1:3000/startBattle/{self.theme}/{token}"
        return urlencode(url)

    def create_teams(self) -> List['Team']:
        team_list = []
        for streamer in self.streamer_list:
            team_list.append(Team(streamer))
        return team_list

    def __str__(self):
        return self.name

    def render(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def get_all_created_battles() -> list['BattleQuizz']:
        battles = BattleQuizz.query.filter_by(status="CREATED").all()
        logger.info(f"Voici mes battles: {battles}")
        return battles

    @staticmethod
    def create_battle(name: str, streamers: list, theme: str, questions_number: int) -> None:
        battle = BattleQuizz(name, streamers, theme, questions_number)
        battle.streamers_number = len(streamers)
        db.session.add(battle)
        db.session.commit()

    @staticmethod
    def get_battle_by_id(unique_id: int) -> 'BattleQuizz':
        battle = BattleQuizz.query.filter_by(id=unique_id).first()
        return battle

    @staticmethod
    def get_battle_by_name(name: str) -> 'BattleQuizz':
        battle = BattleQuizz.query.filter_by(name=name).first()
        logger.info(f"Ma battle par nom: {battle}")
        return battle

    @staticmethod
    def delete_battle_by(unique_id: int) -> None:
        battle = BattleQuizz.query.filter_by(id=unique_id).first()
        db.session.delete(battle)
        db.session.commit()

    @staticmethod
    def start_battle(battle_id: int) -> None:
        battle = BattleQuizz.query.filter_by(id=battle_id).first()
        battle.status = "ACTIVATED"
        db.session.add(battle)
        db.session.commit()

    @staticmethod
    def end_battle(battle_id: int) -> None:
        battle = BattleQuizz.query.filter_by(id=battle_id).first()
        battle.status = "DEACTIVATED"
        db.session.add(battle)
        db.session.commit()

    @staticmethod
    def get_the_quizz_of_the_battle(battle_id: int) -> 'Quizz':
        logger.info("Mais que c'est pénible.....")
        return Quizz.query.filter_by(battle_id=battle_id).first()

    @staticmethod
    def get_teams_of_battle(battle_id: int) -> List[Team]:
        teams = Team.query.filter_by(battle_id=battle_id).all()
        return teams
