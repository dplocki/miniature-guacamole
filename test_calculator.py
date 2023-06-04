import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a, b, expected_result", [(5, 10, 15)])
def test_add(calculator, a, b, expected_result):
    assert calculator.add(a, b) == expected_result
