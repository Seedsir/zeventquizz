from model.db import db
from model.quizz.quizz import Quizz
import uuid
from model.teams.team import Team


class BattleQuizz(db.Model):
    __tablename__ = "battles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    stremers_number = db.Column(db.Integer())

    def __init__(self, streamers_list: list, theme: str, question_number: int):
        self.streamer_list = streamers_list
        self.theme = theme
        self.quizz = Quizz(theme, question_number)
        self.suscribe_url = self.get_suscribe_url()
        self.teams = []

    def get_suscribe_url(self):
        token = uuid.uuid4()
        url = f"http://127.0.0.1:8080/battle/{self.theme}/{token}"
        return url

    def create_teams(self):
        for streamer in self.streamer_list:
            self.teams.append(Team(streamer))

    def get_teams(self):
        if not len(self.teams) > 0:
            return "Aucune équipe n'a été crée pour le moment"
        dict_teams = {}
        for equipe in self.teams:
            dict_teams[f'Equipe {self.teams.index(equipe)}'] = equipe.streamer
        return dict_teams
