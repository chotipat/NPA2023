import pytest
from fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "input, output",
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
def test_fizzbuzz(input, output):
    assert output == fizzbuzz(input)


if __name__ == "__main__":
    print("Please run with pytest")
