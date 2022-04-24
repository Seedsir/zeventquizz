from flask import Flask, render_template, redirect, request, jsonify, make_response, g

from model.battle import BattleQuizz

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("welcome.html")


@app.route("/home")
def home():
    return render_template("home.html")

def get_theme(theme):
    return {
        "label": theme
    }

@app.route('/api/themes', methods=['GET'])
def theme():
    themes = ['Zevent', 'League of Legend', 'Fornite', 'Dark Souls']
    themes = [get_theme(theme) for theme in themes]
    return jsonify(themes)

@app.route("/create_battle", methods=['GET'])
def create_battle():
    themes = ['Zevent', 'League of Legend', 'Fornite', 'Dark Souls']
    r = make_response(
        render_template("create_battle.html", themes=themes)
    )
    r.status = "200"
    return r


@app.route("/battle_suscribe", methods=['POST'])
def battle_suscribe():
    data = request.data
    theme = 'Zevent'
    number_question = 2
    streamer_list = ['Zerator', 'misterMV']
    global battle
    battle = BattleQuizz(streamer_list, theme, number_question)
    battle.get_teams()
    return render_template("battle_suscribe.html", battle=battle)


@app.route("/create_tournament")
def create_tournament():
    return render_template("create_tournament.html")


@app.route("/battle/<theme>/<uuid>")
def quizz(theme, uuid):
    battle.quizz.create_quizz()
    return render_template("quizz.html", battle=battle)


if __name__ == '__main__':
    app.run("0.0.0.0", port=8080, debug=True)
