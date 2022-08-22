from model.users.user import Player
from main import db


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, streamer: str):
        self.streamer = streamer
        self.viewers = []

    def add_viewer(self, user: Player):
        self.viewers.append(user)

    def get_numbers_of_player(self):
        if len(self.viewers) > 0:
            return len(self.viewers)
        return "Aucun joueur n'a rejoint votre équipe pour le moment"
