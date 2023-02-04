from pprint import pprint
import json

import psycopg2

INSERT_QUESTION = """
INSERT INTO questions (value, theme, point, difficulty)
    VALUES ('%s', '%s', %d, '%s');
"""

INSERT_ANSWER = """
INSERT INTO answers (value, is_true, question_id)
    VALUES ('%s', '%s', %d);
"""

SELECT_QUESTION = """
SELECT
    id
FROM
    questions
WHERE
    value = '%s';
"""
if __name__ == '__main__':
    with open("question.json", "r") as openfile:
        source_info = json.load(openfile)

    zevent = psycopg2.connect(
        user='postgres',
        password='zevent',
        host="localhost",
        database="zevent_quizz",
        connect_timeout=5
    )
    cursor = zevent.cursor()
    pprint(source_info)
    for question in source_info['questions']:
        cursor.execute(INSERT_QUESTION % (
            question['question'],
            question['thème'],
            question['nombre_de_points'],
            question['difficulté']
        ))
        cursor.execute(SELECT_QUESTION % (question['question']))
        question_id = cursor.fetchall()[0]
        for reponse in question['réponses']:
            cursor.execute(INSERT_ANSWER % (
                reponse['réponse'],
                reponse['juste'],
                question_id[0],
            ))
    zevent.commit()
    cursor.close()
    zevent.close()
