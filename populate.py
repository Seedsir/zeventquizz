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


def main():
    answers = create_answers(3)
    answers_id = [a["id"] for a in answers]
    create_question(answers_id)
    questions = get_questions()
    print(questions)


if __name__ == "__main__":
    main()
