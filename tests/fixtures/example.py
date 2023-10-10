import pytest


@pytest.fixture
def example_global_fixture():
    value = "example_global_value"
    yield value
