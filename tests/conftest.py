import pytest

@pytest.fixture()
def app():
    from main import Application

    yield Application.app


@pytest.fixture()
def client(app):
    return app.test_client()
