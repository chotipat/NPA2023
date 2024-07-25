from fizzbuzz import fizzbuzz

def test_fizzbuzz(test_input):
    assert 1 == fizzbuzz(test_input[0])
    assert 2 == fizzbuzz(test_input[1])
    assert 'Fizz' == fizzbuzz(test_input[2])
    assert 4 == fizzbuzz(test_input[3])
    assert 'Buzz' == fizzbuzz(test_input[4])
    assert 'Fizz' == fizzbuzz(6)
    assert 7 == fizzbuzz(7)
    assert 'FizzBuzz' == fizzbuzz(15)
    assert 'Fizz' == fizzbuzz(18)
    assert 'Buzz' == fizzbuzz(20)
    assert 'FizzBuzz' == fizzbuzz(30)
    print("All tests are passed.")

if __name__ == '__main__':
    test_fizzbuzz(int(input())
