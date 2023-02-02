from flask import Flask, render_template, request, jsonify, make_response

from utils.constants import THEMES
from models.battles.battle import BattleQuizz


class Application:
    app = Flask(__name__)

    def __init__(self):
        self.battle = None

    @staticmethod
    @app.route("/")
    def index():
        return render_template("welcome.html")

    @staticmethod
    @app.route("/home")
    def home():
        return render_template("home.html")

    ################### THEME ##############################3
    def get_theme(self, theme):
        return {
            "label": theme
        }

    @staticmethod
    @app.route('/api/themes', methods=['GET'])
    def theme():
        themes = [application.get_theme(theme) for theme in THEMES]
        return jsonify(themes)

    ###################################################
    #
    ################ TEAM ##########################

    @staticmethod
    @app.route('/api/team', methods=['GET'])
    def team():
        teams = application.battle.get_teams()
        return jsonify(teams)

    #####################################################

    @staticmethod
    @app.route("/create_battle", methods=['GET'])
    def create_battle():
        themes = ['Zevent', 'League of Legend', 'Fornite', 'Dark Souls']
        r = make_response(
            render_template("create_battle.html", themes=themes)
        )
        r.status = "200"
        return r

    @staticmethod
    @app.route("/battle_suscribe", methods=['POST'])
    def battle_suscribe():
        data = request.data
        theme = 'Zevent'
        number_question = 2
        streamer_list = ['Zerator', 'misterMV']
        application.battle = BattleQuizz(streamer_list, theme, number_question)
        application.battle.create_teams()
        return render_template("battle_suscribe.html", battle=application.battle)

    @staticmethod
    @app.route("/create_tournament")
    def create_tournament():
        return render_template("create_tournament.html")

    @staticmethod
    @app.route("/battle/<theme>/<uuid>")
    def quizz(theme, uuid):
        application.battle.quizz.create_quizz()
        return render_template("quizz.html", battle=application.battle)


if __name__ == '__main__':
    application = Application()
    application.app.run("0.0.0.0", port=8080, debug=True)
