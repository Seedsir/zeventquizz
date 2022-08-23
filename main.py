import psycopg2
from flask_api import FlaskAPI

from model.answers.routes import app as answers_app
from model.battles.routes import app as battles_app
from model.db import db
from model.questions.routes import app as questions_app
from model.quizz.routes import app as quizz_app
from model.teams.routes import app as teams_app
from model.users.routes import app as users_app

from model import User, Quizz, BattleQuizz, Team, Answer


def create_app():

    app = FlaskAPI(__name__)
    app.register_blueprint(questions_app)
    app.register_blueprint(answers_app)
    app.register_blueprint(quizz_app)
    app.register_blueprint(battles_app)
    app.register_blueprint(teams_app)
    app.register_blueprint(users_app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:zevent@db:5432/zevent_quizz"
    db.init_app(app)
    with app.app_context():
        try:
            db.create_all()
        # ignore duplicate errors due to multiple workers running
        except Exception:
            pass
    return app
