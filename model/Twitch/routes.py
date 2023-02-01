from flask import Blueprint, request, jsonify
from model.Twitch.oauth_twitch import TwitchAuth
app = Blueprint("twitch", __name__)


@app.route("/acceuil", methods=['GET'])
def acceuil():
    return jsonify(TwitchAuth.create_user())

@app.route("/login", methods=['GET'])
def login(scope="user:read:email"):
    return TwitchAuth.do_login(scope)


@app.route("/authorisation_code", methods=['GET'])
def get_token():
    code = request.args['code']
    return TwitchAuth.get_token(code)

@app.route("/refresh_token", methods=['GET'])
def get_refresh_token():
    return TwitchAuth.handle_refresh_tocken()