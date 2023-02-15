import pytest
from main import create_app
from models import User, Question, Answer, BattleQuizz, Team, Quizz
from models.db import db


@pytest.fixture()
def app():
    yield create_app()


@pytest.fixture()
def client(app):
    with app.test_request_context():
        yield app.test_client()


@pytest.fixture()
def user():
    user = User("Seedsir", '12345678')
    user.create_user(user.username, '12345678', refresh_token=None)
    last_user = User.query.order_by(User.id.desc()).first()
    user.id = int(last_user.id)
    return user


@pytest.fixture()
def battle():
    battle = BattleQuizz("La battle de la mort",
                         ["Zeratroll", "Sixenus", "DFGood"],
                         "Gérard en ski",
                         20
                         )
    battle.create_battle("La battle de la mort",
                         ["Zeratroll", "Sixenus", "DFGood"],
                         "Gérard en ski",
                         20)
    last_battle = BattleQuizz.query.order_by(BattleQuizz.id.desc()).first()
    battle.id = int(last_battle.id)
    teams = Team.query.filter_by(battle_id=battle.id).all()
    for team in battle.teams:
        for t in teams:
            if team.name == t.name:
                team.id = t.id
    quizz = Quizz.query.filter_by(battle_id=battle.id).first()
    battle.quizz[0].id = quizz.id
    return battle


@pytest.fixture()
def team():
    team = Team("Tidoublou")
    team.create_team("Tidoublou")
    last_insert = Team.query.order_by(Team.id.desc()).first()
    team.id = int(last_insert.id)
    return team


@pytest.fixture()
def question():
    question = Question()
    question.create_question("Est ce que mes tests passent ?", "Tester mon code")
    last_insert = Question.query.order_by(Question.id.desc()).first()
    question.id = int(last_insert.id)
    question.theme = last_insert.theme
    yield question


@pytest.fixture()
def answer():
    answer = Answer.query.order_by(Answer.id.desc()).first()
    yield answer


@pytest.fixture()
def question_with_true_answer():
    question = Question()
    question.create_question("Est ce que mes tests passent avec un bool a true?", "Tester mon code")
    last_insert = Question.query.order_by(Question.id.desc()).first()
    question.id = int(last_insert.id)
    answer = Answer(question.id, "Cette réponse est vraie", True)
    answer.create_answer(question.id, "Cette réponse est vraie", True)
    yield question
