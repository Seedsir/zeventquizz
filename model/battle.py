from model.quizz import Quizz
import uuid

from model.team import Team


class BattleQuizz:

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

    def get_teams(self):
        for streamer in self.streamer_list:
            self.teams.append(Team(streamer))
