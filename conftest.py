import os
import pytest
from run import create_app


@pytest.fixture
def client():
    config = os.environ['APP_SETTINGS']
    app = create_app(config)
    with app.test_client() as client:
        yield client
