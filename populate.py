import requests


base_url = "http://localhost:5000"


def create_answers(nb: int):
    for x in range(nb):
        response = requests.post(base_url + "/answers", json={"label": f"answer {x}"})
        yield response.json()


def create_question(answers):
    response = requests.post(
        base_url + "/questions", json={"label": "Question X", "answers": answers}
    )

    return response.json()


def get_questions():
    return requests.get(base_url + "/questions").json()


def get_answers(question_id):
    return requests.get(base_url + f"/questions/{question_id}/answers").json()


def add_answers(question_id, answer_id):
    return requests.put(
        base_url + f"/questions/{question_id}/answers/{answer_id}"
    ).json()


def main():
    answers = create_answers(3)
    answers_id = [a["id"] for a in answers]
    create_question(answers_id)
    questions = get_questions()
    print(questions)
    response = get_answers(questions[0]["id"])
    print(response)

    response = add_answers(questions[0]["id"], answers_id[0])
    response = get_answers(questions[0]["id"])
    print(response)


if __name__ == "__main__":
    main()
