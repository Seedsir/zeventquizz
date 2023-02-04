import time

from flask_api import FlaskAPI
import sqlalchemy

from models.admin import admin
from models.answers.routes import app as answers_app
from models.battles.routes import app as battles_app
from models.db import db
from models.questions.routes import app as questions_app
from models.quizz.routes import app as quizz_app
from models.teams.routes import app as teams_app
from models.users.routes import app as users_app
from models.Twitch.routes import app as twitch


def create_app():
    app = FlaskAPI(__name__)
    app.secret_key = 'super secret key'
    app.register_blueprint(questions_app)
    app.register_blueprint(answers_app)
    app.register_blueprint(quizz_app)
    app.register_blueprint(battles_app)
    app.register_blueprint(teams_app)
    app.register_blueprint(users_app)
    app.register_blueprint(twitch)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:zevent@db:5432/zevent_quizz"
    db.init_app(app)
    create_database(app)
    admin.init_app(app)

    return app


def create_database(app):
    with app.app_context():
        # to check that we can query the database before trying to create the db
        for i in range(4):
            try:
                db.session.execute('SELECT 1')
            except sqlalchemy.exc.OperationalError:
                time_to_sleep = i * 2
                print(f'Database not started yet, sleeping {time_to_sleep}')
                time.sleep(time_to_sleep)
        db.create_all()
