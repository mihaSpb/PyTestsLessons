import pytest


@pytest.fixture
def set_up():
    print(" Logged in")
    yield
    print("\nLogged out")

def test_sending_mail_1(set_up):
    print("Mail sending")

def test_sending_mail_2(set_up):
    print("Mail sending")
