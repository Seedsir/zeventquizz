from flask import Flask, render_template, redirect, request, jsonify, make_response, g

from model.battle import BattleQuizz

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("welcome.html")


@app.route("/home")
def home():
    return render_template("home.html")













################### THEME ##############################3
def get_theme(theme):
    return {
        "label": theme
    }

@app.route('/api/themes', methods=['GET'])
def theme():
    themes = ['Zevent', 'League of Legend', 'Fornite', 'Dark Souls']
    themes = [get_theme(theme) for theme in themes]
    return jsonify(themes)
###################################################



################ TEAM ##########################

def get_team(team_label):
    return {
        "label": team_label
    }

@app.route('/api/team', methods=['GET'])
def team():
    teams = ['MisterMV', 'Zerator', 'Jacky', 'Michel']
    teams = [get_team(team) for team in teams]
    return jsonify(teams)


#####################################################


############### BATTLE ##############################
def get_mock_battle():
    return {
        "id": 1,
        "questions": [
            {
                "id": 1,
                "label": "En quelle annee est ne bernard ?",
                "answers": [
                    {
                        "id": 1,
                        "label": "1900",
                        'is_right_answer': True
                    },
                    {
                        "id": 2,
                        "label": "1990",
                        'is_right_answer': False
                    },
                    {
                        "id": 3,
                        "label": "1999",
                        'is_right_answer': False
                    }
                ]
            }
        ]
    }

def get_mock_battle_id():
    return {
        "battleId": 1
    }

@app.route('/api/battle', methods=['POST'])
def create_battle_two():
    #TODO: Some backend

    return jsonify(get_mock_battle_id())
    
@app.route('/api/battle/<int:battle_id>', methods=['GET'])
def get_battle(battle_id):
    #TODO: Some backend
    return jsonify(get_mock_battle())



##############################################



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
