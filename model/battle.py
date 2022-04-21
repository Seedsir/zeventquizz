from model.quizz import Quizz
import requests
import uuid

from model.team import Team


class BattleQuizz:

    def __init__(self, streamers_list: list, theme: str, question_number: int):
        self.streamer_list = streamers_list
        self.theme = theme
        self.quizz = Quizz(theme, question_number).create_quizz()
        self.suscribe_url = self.suscribe_url()
        self.teams = []

    def suscribe_url(self):
        token = uuid.uuid4()
        return f"http://127.0.0.1:8080/battle/{self.theme}/{token}"

    def define_team(self):
        for streamer in self.streamer_list:
            self.teams.append(Team(streamer))





