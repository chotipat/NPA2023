import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("num", range(1, 16))
def test_fizzbuzz(num):
    result = fizzbuzz(num)
    if num in [3, 6, 9, 12]:
        assert 'Fizz' == result
    elif num in [5, 10]:
        assert 'Buzz' == result
    elif num in [15]:
        assert 'FizzBuzz' == result
    else:
        assert num == result
    print("All tests are passed.")

if __name__ == '__main__':
    test_fizzbuzz(int(input()))
