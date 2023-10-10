import pytest


@pytest.fixture
def example_unit_fixture():
    value = "example_unit_value"
    yield value
