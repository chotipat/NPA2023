import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("num", range(1, 31))
def test_fizzbuzz(num):
    result = fizzbuzz(num)
    if num%3 == 0 and num%5 == 0:
        assert 'FizzBuzz' == result
    elif num%3 == 0:
        assert 'Fizz' == result
    elif num%5 == 0:
        assert 'Buzz' == result
    else:
        assert num == result
    print("All tests are passed.")

if __name__ == '__main__':
    test_fizzbuzz()
