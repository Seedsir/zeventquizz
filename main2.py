from flask_api import FlaskAPI

from questions.routes import questions_app

app = FlaskAPI(__name__)

app.register_blueprint(questions_app)


def main():
    app.run("0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
