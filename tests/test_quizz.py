import pytest

from models.quizz import Quizz


def test_create_quizz():
    quizz_test_failed = Quizz("Robert", 4)
    with pytest.raises(FileNotFoundError) as exception:
        quizz_test_failed.create_quizz()
        assert exception.value == "Merci de vérifier le thème choisi"

def test_quizz_size():
    quizz = Quizz("Zevent", 150)
    with pytest.raises(ValueError) as ve:
        quizz.create_quizz()
        assert ve.value == "Le nombre de question est trop important"

def test_progress_quizz():
    quizz = Quizz("Zevent", 24)
    index = 1
    assert isinstance(index / quizz.question_number * 100, float)
    progress = quizz.quizz_progress(index)
    assert isinstance(progress, int)
