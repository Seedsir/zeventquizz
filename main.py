from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

from model.questions.routes import app as questions_app
from model.answers.routes import app as answers_app
from model.quizz.routes import app as quizz_app
from model.battles.routes import app as battles_app
from model.teams.routes import app as teams_app
from model.users.routes import app as users_app

db = None


def create_app():
    global db
    app = FlaskAPI(__name__)
    app.register_blueprint(questions_app)
    app.register_blueprint(answers_app)
    app.register_blueprint(quizz_app)
    app.register_blueprint(battles_app)
    app.register_blueprint(teams_app)
    app.register_blueprint(users_app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:zevent@mescouilles:5432/zevent_quizz"
    db = SQLAlchemy(app)
    db.create_all()
    return app
