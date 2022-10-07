from model.db import db
from model.users.user import Player


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                        nullable=True)
    battle_id = db.Column(db.Integer, db.ForeignKey('battles.id'),
                          nullable=True)

    def __init__(self, streamer: str):
        self.streamer = streamer
        self.viewers = []

    def add_viewer(self, user: Player):
        self.viewers.append(user)

    def get_numbers_of_player(self):
        if len(self.viewers) > 0:
            return len(self.viewers)
        return "Aucun joueur n'a rejoint votre équipe pour le moment"

    def render(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def get_teams(battle_id: int) -> list['Team']:
        teams = Team.query.filter_by(battle_id=battle_id).all()
        return teams

    @staticmethod
    def get_team_by_id(team_id: int) -> 'Team':
        team = Team.query.filter_by(id=team_id).first()
        return team

    @staticmethod
    def create_team(streamer: str) -> None:
        team = Team(streamer)
        db.session.add(team)
        db.session.commit()

    @staticmethod
    def delete_team_by_id(team_id: int) -> None:
        team = Team.query.filter_by(id=team_id).first()
        db.session.delete(team)
        db.session.commit()
