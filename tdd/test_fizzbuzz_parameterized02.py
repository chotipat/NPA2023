import pytest
from fizzbuzz import fizzbuzz


def test_data(request):
    return request.param


@pytest.mark.parametrize(
    "testdata",
    [
        (1, 1),
        (2, 2),
        (3, "Fizz"),
        (4, 4),
        (5, "Buzz"),
        (6, "Fizz"),
        (7, 7),
        (8, 8),
        (9, "Fizz"),
        (10, "Buzz"),
        (11, 11),
        (12, "Fizz"),
        (13, 13),
        (14, 14),
        (15, "FizzBuzz"),
    ],
)
def test_fizzbuzz(test_data):
    input_data, output_data = test_data
    assert output_data == fizzbuzz(input_data)


if __name__ == "__main__":
    print("Please run with pytest")
