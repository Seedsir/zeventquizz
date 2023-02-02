import requests
import json
from urllib.parse import urlencode
from utils.constants import CLIENT_ID,CLIENT_SECRET

from flask_api import FlaskAPI
from flask import redirect, request


class TwitchAuth:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = None

    def get_authorization_url(self, scope):
        auth_url = "https://id.twitch.tv/oauth2/authorize"
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": scope
        }
        url = auth_url + "?" + urlencode(params)
        return url

    def get_access_token(self, code):
        token_url = "https://id.twitch.tv/oauth2/token"
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
        return requests.post(token_url, data=data, headers=headers)

    def get_refresh_token(self, refresh_token):
        token_url = "https://id.twitch.tv/oauth2/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        return requests.post(token_url, data=data, headers=headers)


app = FlaskAPI(__name__)

@app.route("/acceuil", methods=['GET'])
def acceuil():
    return get_user()


@app.route("/login", methods=['GET'])
def login():
    auth = TwitchAuth(CLIENT_ID, CLIENT_SECRET,
                      "http://localhost:5000/authorisation_code")
    url = auth.get_authorization_url("user:read:email")
    return redirect(url)


@app.route("/authorisation_code", methods=['GET'])
def get_token():
    code = request.args['code']
    twitch = TwitchAuth(CLIENT_ID, CLIENT_SECRET,
                        "http://localhost:5000/authorisation_code")
    twitch_response = twitch.get_access_token(code)
    if twitch_response.status_code == 401:
        get_refresh_token()
    token = twitch_response.json()['access_token']
    refresh_token = twitch_response.json()['refresh_token']
    with open("/home/besposito/Documents/test/zeventquizz/tmp/token.txt", "w") as file:
        file.write(token)
    with open("/home/besposito/Documents/test/zeventquizz/tmp/refresh_token.txt", "w") as file:
        file.write(refresh_token)
    return redirect("/acceuil")

@app.route("/refresh_token", methods=['GET'])
def get_refresh_token():
    refresh_token_file = open("/home/besposito/Documents/test/zeventquizz/tmp/refresh_token.txt", "r")
    refresh_token = refresh_token_file.read()
    twitch = TwitchAuth("", "",
                        "http://localhost:5000/authorisation_code")
    twitch_response = twitch.get_refresh_token(refresh_token).json()
    token = twitch_response['access_token']
    with open("/home/besposito/Documents/test/zeventquizz/tmp/token.txt", "w") as file:
        file.write(token)
    return redirect("/acceuil")

def get_user():

    token_file = open("/home/besposito/Documents/test/zeventquizz/tmp/token.txt", "r")
    token = token_file.read()
    data = {
        "Authorization": f"Bearer {token}",
        "Client-Id": CLIENT_ID
    }
    req = requests.get("https://api.twitch.tv/helix/users", headers=data)
    user_id = req.json()["data"][0].get("id")
    username = req.json()["data"][0].get("display_name")
    profile_image = req.json()["data"][0].get("profile_image_url")
    if profile_image is None:
        # TODO trouver une url de logo par default
        pass
    return req.json()


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)