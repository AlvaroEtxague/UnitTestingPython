import pytest


def setup_module(module):
    print("\nSetting up module")


def teardown_module(module):
    print("Tearing down module")


def setup_function(function):
    if function == test_one:
        print("\nSetting up test_one")
    elif function == test_two:
        print("\nSetting up test_two")
    else:
        print("\nSetting up unknown test")


def teardown_function(function):
    if function == test_one:
        print("Tearing down test_one")
    elif function == test_two:
        print("Tearing down test_two")
    else:
        print("Tearing down unknown test")


def test_one():
    print("Executing test_one")
    assert True


def test_two():
    print("Executing test_two")
    assert True
