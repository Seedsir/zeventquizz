from flask import Flask, render_template, redirect, request, jsonify
import json
import requests

from constants import CLIENT_ID, ACCESS_TOKEN, CONNEXION_URL
from model.quizz import Quizz
from model.users import User

app = Flask(__name__)

def get_label():
    import uuid
    return str(uuid.uuid4())

def get_answer():
    return {
        "label": get_label(),
        "is_right_answer": True
    }

def get_questions():
    return {
        'label': get_label(),
        'answer': [get_answer() for x in range(3)]
    }

def get_quizz():
    return {
        'id': 1,
        'label': get_label(),
        'questions': [get_questions() for x in range(10)]
    }

@app.route('/quizz', methods=['GET'])
def quizz():
    quizz = [get_quizz() for _ in range(10)]
    return jsonify(quizz)

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
    return redirect(CONNEXION_URL)


@app.route("/connected")
def connected():
    return render_template("redirect.html")


@app.route("/home")
def home():
    access_token = request.args.get("access_token")
    if access_token is None:
        raise NotImplementedError
    user = User()
    user.get_user()
    return user.__dict__


if __name__ == '__main__':
    app.run("0.0.0.0", port=8080, debug=True)