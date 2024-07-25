import pytest
from fizzbuzz import fizzbuzz


@pytest.fixture(params=[(1, 1), (2, 2), (3, "Fizz"), (4, 4), (5, "Buzz")])
def test_data(request):
    return request.param


def test_fizzbuzz(test_data):
    input_data, output_data = test_data
    assert fizzbuzz(input_data) == output_data


if __name__ == "__main__":
    print("Please run with pytest")
