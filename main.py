from flask_api import FlaskAPI

from model.questions.routes import app as questions_app
from model.answers.routes import app as answers_app
from model.quizz.routes import app as quizz_app
from model.battles.routes import app as battles_app
from model.teams.routes import app as teams_app
from model.users.routes import app as users_app

app = FlaskAPI(__name__)

app.register_blueprint(questions_app)
app.register_blueprint(answers_app)
app.register_blueprint(quizz_app)
app.register_blueprint(battles_app)
app.register_blueprint(teams_app)
app.register_blueprint(users_app)


def main():
    app.run("0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
