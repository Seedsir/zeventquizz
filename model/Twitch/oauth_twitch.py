import requests
from urllib.parse import urlencode
from flask import redirect
from utils.constants import CLIENT_ID, CLIENT_SECRET
from model.users.user import User


class TwitchAuth:
    auth_url = "https://id.twitch.tv/oauth2/authorize"
    token_url = "https://id.twitch.tv/oauth2/token"
    redirect_uri = "http://localhost:5000/authorisation_code"
    users_url = "https://api.twitch.tv/helix/users"

    def __init__(self, client_id, client_secret):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.access_token = None
        self.refresh_token = None

    def get_authorization_url(self, scope):
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": scope
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

    def do_login(self, scope):
        url = self.get_authorization_url(scope)
        return redirect(url)

    def get_token(self, code):
        twitch_response = self.get_access_token(code)
        if twitch_response.status_code == 401:  # TODO gérer le cas ou le refresh est None
            self.get_refresh_token(self.refresh_token)
        self.token = twitch_response.json()['access_token']
        self.refresh_token = twitch_response.json()['refresh_token']
        return redirect("/acceuil")

    def handle_refresh_tocken(self):
        twitch_response = self.get_refresh_token(self.refresh_token)
        self.token = twitch_response.json()['access_token']
        self.refresh_token = twitch_response.json()['refresh_token']
        return redirect("/acceuil")

    def create_user(self):
        data = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": CLIENT_ID
        }
        req = requests.get(self.users_url, headers=data)
        user_id = req.json()["data"][0].get("id")
        username = req.json()["data"][0].get("display_name")
        profile_image = req.json()["data"][0].get("profile_image_url")
        if profile_image is None:
            # TODO trouver une url de logo par default
            pass
        user = User(username)
        return user.render()
