#TODO Work in progress
# from flask import Blueprint, request
#
# app = Blueprint("quizz_app", __name__)
#
# manager = QuizzManager()
#
#
# @app.route("/quizz", methods=["GET"])
# def get_all():
#     return manager.get_all()
#
#
# @app.route("/quizz", methods=["POST"])
# def create_answer():
#     body = request.get_json()
#     return manager.create(body)
#
#
# @app.route("/quizz/<answer_id>", methods=["GET"])
# def get_answer(answer_id):
#     return manager.get(answer_id)
#
#
# @app.route("/quizz/<answer_id>", methods=["DELETE"])
# def delete_answer(answer_id):
#     return manager.delete(answer_id)
