import pytest


def test_can_assert_true():
    assert True


def fizzbuzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"
    return str(value)


def is_multiple(value, mod):
    return (value % mod) == 0


def check_fizzbuzz(value, expected_ret_value):
    returned_value = fizzbuzz(value)
    assert returned_value == expected_ret_value


# Step 1
def test_can_call_fizzbuzz():
    fizzbuzz(1)


# Step 2
def test_returns_1_with_1_passed_in():
    check_fizzbuzz(1, "1")


# Step 3
def test_returns_2_with_2_passed_in():
    check_fizzbuzz(2, "2")


# Step 4
def test_returns_fizz_with_3_passed_in():
    check_fizzbuzz(3, "Fizz")


# Step 5
def test_returns_buzz_with_5_passed_in():
    check_fizzbuzz(5, "Buzz")


# Step 6
def test_returns_fizz_with_multiple_of_3_passed_in():
    check_fizzbuzz(6, "Fizz")


# Step 7
def test_returns_buzz_with_multiple_of_5_passed_in():
    check_fizzbuzz(10, "Buzz")


# Step 8
def test_returns_fizzbuzz_with_15_passed_in():
    check_fizzbuzz(15, "FizzBuzz")

