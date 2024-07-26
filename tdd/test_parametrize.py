import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (5, 7, 12),
        (-2, 2, 0),
    ],
)
def test_addition(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        (2, 3),
        (5, 7),
        (-2, 2),
    ],
)
def test_positive_numbers(a, b):
    assert a > 0
    assert b > 0
