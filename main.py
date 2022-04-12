from flask import Flask
import json

from model.quizz import Quizz

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

if __name__ == '__main__':
    app.run("0.0.0.0", port=8080, debug=True)