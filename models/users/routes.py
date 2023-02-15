import requests
from flask import Blueprint, request, abort, Response

from models.users.user import User
from flask import jsonify

from utils.constants import CLIENT_ID

app = Blueprint("users", __name__)


# TODO def admin_route(User)
# if user.admin == True bah OK
# elif vers une page d'acceuil
# il fait que ca check sir le user est admin pour acceder

@app.route("/users/<username>", methods=["GET"])
def get_user(username: str) -> 'Response':
    return jsonify([User.get_user_by_username(username).render()])


@app.route("/users/user/<id_twitch>", methods=["GET"])
def get_user_by_id_twitch(id_twitch: int) -> 'Response':
    list_users = []
    user = [user for user in User.get_user_by_id_twitch(str(id_twitch))][0].render()
    list_users.append(user)
    return jsonify(list_users)


@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id: int) -> 'Response':
    User.delete_user(user_id)
    return jsonify([{"status": 200, "message": "User deleted"}])


@app.route("/users/my_profile", methods=["GET"])
def get_profile() -> 'Response':
    access_token = request.headers.get('token')
    if access_token is None:
        return abort(403)
    data = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": CLIENT_ID
    }
    req = requests.get('https://api.twitch.tv/helix/users', headers=data)
    if req.status_code != 200:
        return jsonify([{
            "status_code": req.status_code,
            "message": req.text
        }])
    user_id = req.json()["data"][0].get("id")
    return jsonify(User.get_user_by_id_twitch(user_id).render())
