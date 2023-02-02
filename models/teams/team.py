from models.db import db
from models.users.user import Player, User

teams_users = db.Table('teams_users',
                       db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key=True),
                       db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
                       )


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    battle_id = db.Column(db.Integer, db.ForeignKey('battles.id'),
                          nullable=True)
    users = db.relationship('User', secondary=teams_users, lazy='subquery',
                           backref=db.backref('users', lazy=True))

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

    def __str__(self):
        return self.name

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

    @staticmethod
    def add_player_to_team(team_id: int, user_id: int) -> None:
        team = Team.query.filter_by(id=team_id).first()
        user = User.query.filter_by(id=user_id).first()
        print(dir(team))
        print("Salut c'est moi")
        user.team.id = team.id
        db.session.add(user)
        db.session.commit()
