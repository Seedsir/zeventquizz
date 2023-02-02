from http.client import HTTPException

import requests
from flask import Blueprint, request, abort

from model.users.user import User
from flask import jsonify

from utils.constants import CLIENT_ID

app = Blueprint("users", __name__)



#TODO def admin_route(User)
    #if user.admin == True bah OK
    #elif vers une page d'acceuil
    # il fait que ca check sir le user est admin pour acceder

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    return jsonify(User.get_user_by_username(username).render())


@app.route("/users/<username>", methods=["DELETE"])
def delete_user(username):
    return User.delete_user_username(username)


@app.route("/users/my_profile", methods=["GET"])
def get_profile():
    access_token = request.headers.get('token')
    if access_token is None:
        return abort(403)
    data = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": CLIENT_ID
    }
    req = requests.get('https://api.twitch.tv/helix/users', headers=data)
    if req.status_code != 200:
        return abort(401)
    user_id = req.json()["data"][0].get("id")
    return jsonify(User.get_user_by_id_twitch(user_id).render())
