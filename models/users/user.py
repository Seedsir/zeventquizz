from typing import Optional

from models.db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    profile_image = db.Column(db.String())
    id_twitch = db.Column(db.String(), nullable=True)
    refresh_token = db.Column(db.String())
    battle = db.relationship('BattleQuizz', backref='user', lazy=True)
    team_id = db.Column(db.Integer, nullable=True)
    # TODO ajouter le team_id

    def __init__(self, username: str, id_twitch: str):
        self.user_id = None
        self.username = username
        self.profile_image = None
        self.id_twitch = id_twitch
        self.refresh_token = None

    def __str__(self):
        return self.username

    def render(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def create_user(username: str, id_twitch: str, refresh_token: Optional[str]) -> None:
        user = User(username, id_twitch)
        user.refresh_token = refresh_token
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_username(username: str) -> 'User':
        user = User.query.filter_by(username=username).first()
        return user

    @staticmethod
    def get_user_by_id_twitch(id_twitch: str) -> list['User']:
        users = User.query.filter_by(id_twitch=id_twitch).all()
        return users

    @staticmethod
    def is_user_already_exist(id_twitch: str) -> bool:
        user = User.query.filter_by(id_twitch=id_twitch).first()
        if user is not None:
            return True

    @staticmethod
    def update_user_username(username: str, new_username: str) -> None:
        user = User.query.filter_by(username=username).first()
        user.username = new_username
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def save_user(user: 'User') -> None:
        old_user = User.query.filter_by(id_twitch=user.id_twitch).first()
        old_user.profile_image = user.profile_image
        old_user.refresh_token = user.refresh_token
        db.session.add(old_user)
        db.session.commit()

    @staticmethod
    def delete_user(user_id: int) -> None:
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def select_a_team(username, battle_id, team_name) -> None:
        user = User.query.filter_by(username=username).first()
        user.battle = battle_id
        user.team = team_name
        db.session.add(user)
        db.session.commit()



class Player(User):

    def __init__(self, username: str, id_twitch: str):
        super().__init__(username, id_twitch)
        self.admin = False


class Streamer(User):

    def __init__(self, username: str, id_twitch: str):
        super().__init__(username, id_twitch)
        self.admin = True
