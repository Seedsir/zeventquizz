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

    def __init__(self):
        self.user_id = None
        self.username = None
        self.profile_image = None

    def connect_user(self):
        return CONNEXION_URL

    def get_user(self):
        data = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Client-Id": CLIENT_ID
        }
        req = requests.get("https://api.twitch.tv/helix/users", headers=data)
        if req.status_code == 200:
            self.user_id = req.json()["data"][0].get("id")
            self.username = req.json()["data"][0].get("display_name")
            self.profile_image = req.json()["data"][0].get("profile_image_url")
            if self.profile_image is None:
                # TODO trouver une url de logo par default
                pass


class Player(User):

    def __init__(self):
        super(Player, self).__init__()


class Streamer(User):

    def __init__(self):
        super(Streamer, self).__init__()
