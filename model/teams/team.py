from model.users.user import Player


class Team:

    def __init__(self, streamer: str):
        self.streamer = streamer
        self.viewers = []

    def add_viewer(self, user: Player):
        self.viewers.append(user)

    def get_numbers_of_player(self):
        if len(self.viewers) > 0:
            return len(self.viewers)
        return "Aucun joueur n'a rejoint votre équipe pour le moment"