import pytest


@pytest.fixture
def setup_teardown():
    print("\nSetup testing")
    yield
    print("\nClean testing")
