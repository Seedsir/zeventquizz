from flask import Blueprint, request

from model.users.manager import UserManager


app = Blueprint("users", __name__)


user_manager = UserManager()


@app.route("/users", methods=["GET"])
def get_all():
    return user_manager.get_all()


@app.route("/users", methods=["POST"])
def create_user():
    body = request.get_json()
    return user_manager.create(body)


@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    return user_manager.get(user_id)


@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return user_manager.delete(user_id)
