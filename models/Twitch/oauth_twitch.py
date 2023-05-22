import requests
from urllib.parse import urlencode
from flask import redirect
from utils.constants import CLIENT_ID, CLIENT_SECRET
from models.users.user import User
from utils.constants import SCOPE

from loguru import logger

class TwitchAuth:
    auth_url = "https://id.twitch.tv/oauth2/authorize"
    token_url = "https://id.twitch.tv/oauth2/token"
    redirect_uri = "http://localhost:5000/authorisation_code"
    users_url = "https://api.twitch.tv/helix/users"

    def __init__(self):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.access_token = None
        self.refresh_token = None

    def get_authorization_url(self):
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": SCOPE
        }
        url = self.auth_url + "?" + urlencode(params)
        return url

    def get_access_token(self, code):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        return requests.post(self.token_url, data=data, headers=headers)

    def get_refresh_token(self, refresh_token):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        return requests.post(self.token_url, data=data, headers=headers)

    @staticmethod
    def do_login():
        twitch = TwitchAuth()
        url = twitch.get_authorization_url()
        return redirect(url)

    @staticmethod
    def get_token(code):
        twitch = TwitchAuth()
        twitch_response = twitch.get_access_token(code)
        if twitch_response.status_code == 401:  # TODO gérer le cas ou le refresh est None
            TwitchAuth.handle_refresh_tocken()
        twitch.access_token = twitch_response.json()['access_token']
        twitch.refresh_token = twitch_response.json()['refresh_token']
        twitch.create_user(twitch)
        return redirect(f'http://localhost:3000/authorisationCode/{twitch.access_token}') # TODO doit communiquer avec le front le token


    @staticmethod
    def handle_refresh_tocken():
        twitch = TwitchAuth()
        twitch_response = twitch.get_refresh_token(twitch.refresh_token)
        twitch.token = twitch_response.json()['access_token']
        twitch.refresh_token = twitch_response.json()['refresh_token']
        return redirect("/acceuil")

    @staticmethod
    def create_user(twitch: 'TwitchAuth') -> User:
        data = {
            "Authorization": f"Bearer {twitch.access_token}",
            "Client-Id": CLIENT_ID
        }
        req = requests.get(twitch.users_url, headers=data)
        user_id = req.json()["data"][0].get("id")
        username = req.json()["data"][0].get("display_name")
        profile_image = req.json()["data"][0].get("profile_image_url")
        user = User(username, user_id)
        if profile_image is None:
            user.profile_image = "https://us.123rf.com/450wm/kchung/kchung1504/kchung150400781/38556950-3d-vert-n%C3%A9on-de-lumi%C3%A8re-lettre-z-isol%C3%A9-sur-fond-noir.jpg"
        if not user.is_user_already_exist(user_id):
            logger.info("L'utilisateur n'existe pas et donc va être créé")
            user.create_user(username, user_id, twitch.refresh_token)
            return user.render()
        user = user.get_user_by_id_twitch(user_id)
        logger.info(f"L'utilisateur existe et les données sont récupéré en db. Type de user: {type(user)} et sa valeur: {user}")
        user.refresh_token = twitch.refresh_token
        user.profile_image = profile_image
        user.save_user(user)
        return user.render()
