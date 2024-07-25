import pytest
from fizzbuzz import fizzbuzz


@pytest.fixture(params=list(range(1, 31)))
def test_input(request):
    return request.param


def test_fizz(test_input):
    if test_input % 3 == 0 and test_input % 5 != 0:
        assert fizzbuzz(test_input) == "Fizz"


def test_buzz(test_input):
    if test_input % 5 == 0 and test_input % 3 != 0:
        assert fizzbuzz(test_input) == "Buzz"


def test_fizzbuzz(test_input):
    if test_input % 3 == 0 and test_input % 5 == 0:
        assert fizzbuzz(test_input) == "FizzBuzz"


def test_others(test_input):
    if test_input % 3 != 0 and test_input % 5 != 0:
        assert fizzbuzz(test_input) == test_input


if __name__ == "__main__":
    test_fizzbuzz(int(input()))
