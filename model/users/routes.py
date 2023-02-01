from flask import Blueprint

from model.users.user import User
from flask import jsonify
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
