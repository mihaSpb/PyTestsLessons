import pytest


@pytest.fixture
def set_up():
    print(" Logged in")
    yield
    print("\nLogged out")

@pytest.fixture(scope="module")
def some():
    print("Запуск до всех тестов")
    yield
    print("Завершение после всех тестов")

@pytest.fixture(scope="function")
def some_function():
    print("Запуск в каждом тесте")
    yield
    print("Завершение после каждого теста")