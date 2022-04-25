import pytest


@pytest.fixture()
def setup1():
    print("\nSetup 1 Fixture")
    yield
    print("\nTeardown 1 Fixture")


@pytest.fixture()
def setup2(request):
    print("\nSetup 2 Fixture")

    def teardown_1():
        print("\nTeardown 1 in setup 2")

    def teardown_2():
        print("\nTeardown 2 in setup 2")

    request.addfinalizer(teardown_1)
    request.addfinalizer(teardown_2)


def test1(setup1):
    print("\nExecuting Test 1")
    assert True


def test2(setup2):
    print("\nExecuting Test 2")
    assert True
