from flask import Blueprint, request, jsonify
from models.Twitch.oauth_twitch import TwitchAuth

app = Blueprint("twitch", __name__)


@app.route("/acceuil", methods=['GET'])
def acceuil():
    return f'Hello world'


@app.route("/login", methods=['GET'])
def login():
    return TwitchAuth.do_login()


@app.route("/authorisation_code", methods=['GET'])
def get_token():
    code = request.args['code']
    return TwitchAuth.get_token(code)


@app.route("/refresh_token", methods=['GET'])
def get_refresh_token():
    return TwitchAuth.handle_refresh_tocken()
