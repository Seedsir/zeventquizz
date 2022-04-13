from flask import Flask, render_template, redirect, request, request_finished
import json
import requests

from constants import CLIENT_ID, ACCESS_TOKEN
from model.quizz import Quizz
from model.users import User

app = Flask(__name__)


@app.route("/")
def index():
    mon_dict = {"test": "Alors"}
    quizz = Quizz("Zevent", 3)
    quizz.create_quizz()
    for question in quizz.questions:
        index = str(quizz.questions.index(question))
        mon_dict["iteration-{}".format(index)] = question.__dict__
    return mon_dict


@app.route("/test_connect", methods=['GET'])
def test_connect():
    return render_template("test_connect.html")


@app.route("/redirect_connect", methods=["GET"])
def connect():
    user = User()
    return redirect(user.connect_user())


@app.route("/connected")
def connected():
    url = request.full_path
    print(url)
    return "Prout"


if __name__ == '__main__':
    app.run("0.0.0.0", port=8080, debug=True)