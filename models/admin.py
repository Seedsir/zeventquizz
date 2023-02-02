from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import User, Answer, BattleQuizz, Quizz, Team, Question

from models.db import  db

admin = Admin()
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(BattleQuizz, db.session))
admin.add_view(ModelView(Team, db.session))
admin.add_view(ModelView(Quizz, db.session))
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(Answer, db.session))