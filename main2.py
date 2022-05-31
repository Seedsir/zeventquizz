from flask_api import FlaskAPI

from questions.routes import app as questions_app
from answers.routes import app as answer_app
from quizz.routes import app as quizz_app

app = FlaskAPI(__name__)

app.register_blueprint(questions_app)
app.register_blueprint(answer_app)
app.register_blueprint(quizz_app)


def main():
    app.run("0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
