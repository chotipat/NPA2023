from fizzbuzz import fizzbuzz


def test_num():
    assert 1 == fizzbuzz(1)
    assert 2 == fizzbuzz(2)
    assert 4 == fizzbuzz(4)
    assert 7 == fizzbuzz(7)
    print("test_num passed")


def test_fizz():
    assert "Fizz" == fizzbuzz(3)
    assert "Fizz" == fizzbuzz(6)
    assert "Fizz" == fizzbuzz(18)
    print("test_fizz passed")


def test_buzz():
    assert "Buzz" == fizzbuzz(5)
    assert "Buzz" == fizzbuzz(20)
    print("test_buzz passed")


def test_fizzbuzz():
    assert "FizzBuzz" == fizzbuzz(15)
    assert "FizzBuzz" == fizzbuzz(30)
    print("test_fizzbuzz passed")


if __name__ == "__main__":
    test_num()
    test_fizz()
    test_buzz()
    test_fizzbuzz()
    print("All tests are passed.")
