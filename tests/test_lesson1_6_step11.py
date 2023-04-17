import pytest
from selenium.common.exceptions import NoSuchElementException
from lessons.lesson1_6_step11 import RegisterForm


link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'


def test_registrate_valid():
    some_web_client = RegisterForm(link1)
    welcome_text = some_web_client.get_welcome_text()
    assert 'Congratulations! You have successfully registered!' == welcome_text


def test_registrate_invalid():
    some_web_client = RegisterForm(link2)
    with pytest.raises(NoSuchElementException):
        welcome_text = some_web_client.get_welcome_text()
        pytest.fail('Must not tu be "Last_name" field')
