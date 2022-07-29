import pytest

@pytest.fixture()
def app():
    from utils.main_to_delete import Application

    yield Application.app


@pytest.fixture()
def client(app):
    return app.test_client()
