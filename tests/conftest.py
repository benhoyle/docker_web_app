"""Settings to allow testing of celery tasks."""
import pytest

# We don't need the line below if we have pip installed pytest-celery
# pytest_plugins = ("celery.contrib.pytest", )


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': 'memory://localhost/',
        'result_backend': 'memory://localhost/',
    }



