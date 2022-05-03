import pytest

@pytest.fixture()
def app():
    from main import application

    yield application


@pytest.fixture()
def client(app):
    return app.test_client()
