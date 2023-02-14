from models.db import db


class Score(db.Model):
    __tablename__ = "scores"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    battle_id = db.Column(db.Integer, db.ForeignKey('battles.id'))  # TODO retirer la foreign key

    def __init__(self, value: int, team_id: int, battle_id=None):
        self.value = value
        self.team_id = team_id
        self.battle_id = battle_id

    def calculate_score(self, point: int) -> int:
        self.value += point
        return self.value

    def __str__(self):
        return f"Votre score est de {self.value}"

    def render(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
