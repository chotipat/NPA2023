import pytest
from fizzbuzz import fizzbuzz


@pytest.fixture
def setup_teardown():
    print("\nSetup testing")
    yield
    print("\nClean testing")


@pytest.mark.num
def test_num(setup_teardown):
    assert 1 == fizzbuzz(1)
    assert 2 == fizzbuzz(2)
    assert 4 == fizzbuzz(4)
    assert 7 == fizzbuzz(7)


@pytest.mark.fizz
def test_fizz(setup_teardown):
    assert "Fizz" == fizzbuzz(3)
    assert "Fizz" == fizzbuzz(6)
    assert "Fizz" == fizzbuzz(18)


@pytest.mark.buzz
def test_buzz(setup_teardown):
    assert "Buzz" == fizzbuzz(5)
    assert "Buzz" == fizzbuzz(20)


@pytest.mark.fizzbuzz
def test_fizzbuzz(setup_teardown):
    assert "FizzBuzz" == fizzbuzz(15)
    assert "FizzBuzz" == fizzbuzz(30)


if __name__ == "__main__":
    test_num()
    test_fizz()
    test_buzz()
    test_fizzbuzz()
    print("All tests are passed.")
