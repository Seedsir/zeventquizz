from model.db import db
from utils.constants import CONNEXION_URL, ACCESS_TOKEN, CLIENT_ID
import requests


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    profile_image = db.Column(db.String())
    team = db.relationship('Team', backref='user', lazy=True)
    battle = db.relationship('BattleQuizz', backref='user', lazy=True)

    def __init__(self, username: str):
        self.user_id = None
        self.username = username
        self.profile_image = None

    def __str__(self):
        return self.username

    def render(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def create_user(username: str) -> None:
        user = User(username)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_username(username: str) -> 'User':
        user = User.query.filter_by(username=username).first()
        return user

    @staticmethod
    def update_user_username(username: str, new_username: str) -> None:
        user = User.query.filter_by(username=username).first()
        user.username = new_username
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def delete_user_username(username: str) -> None:
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def select_a_team(username, battle_id, team_name) -> None:
        user = User.query.filter_by(username=username).first()
        user.battle = battle_id
        user.team = team_name
        db.session.add(user)
        db.session.commit()

    # def connect_user(self):
    #     return CONNEXION_URL
    #
    # def get_user(self):
    #     data = {
    #         "Authorization": f"Bearer {ACCESS_TOKEN}",
    #         "Client-Id": CLIENT_ID
    #     }
    #     req = requests.get("https://api.twitch.tv/helix/users", headers=data)
    #     if req.status_code == 200:
    #         self.user_id = req.json()["data"][0].get("id")
    #         self.username = req.json()["data"][0].get("display_name")
    #         self.profile_image = req.json()["data"][0].get("profile_image_url")
    #         if self.profile_image is None:
    #             # TODO trouver une url de logo par default
    #             pass


class Player(User):

    def __init__(self, username: str):
        super().__init__(username)
        self.admin = False


class Streamer(User):

    def __init__(self, username: str):
        super().__init__(username)
        self.admin = True
