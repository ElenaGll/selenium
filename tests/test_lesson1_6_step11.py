import allure
import pytest
from selenium.common.exceptions import NoSuchElementException


@allure.feature('Stepik test')
@allure.story('Registration valid form')
def test_get_welcome_text(browser):
    link = 'http://suninjuly.github.io/registration1.html'
    browser.get(link)

    first_name = browser.find_element(by='css selector', value='div.first_block input.form-control.first')
    first_name.send_keys('Elena')

    last_name = browser.find_element(by='css selector', value='div.first_block input.form-control.second')
    last_name.send_keys('Donyakina')

    email = browser.find_element(by='css selector', value='div.first_block input.form-control.third')
    email.send_keys('home@gmail.com')

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()

    with allure.step('Successful registration'):
        welcome_text_elt = browser.find_element(by='tag name', value='h1')
        welcome_text = welcome_text_elt.text
        assert 'Congratulations You have successfully registered!' == welcome_text


@allure.story('Registration invalid form')
def test_not_element_last_name(browser):
    link = 'http://suninjuly.github.io/registration2.html'
    browser.get(link)

    first_name = browser.find_element(by='css selector', value='div.first_block input.form-control.first')
    first_name.send_keys('Elena')

    with allure.step('Invalid registration'):
        with pytest.raises(NoSuchElementException):
            browser.find_element(by='css selector', value='div.first_block input.form-control.second')
            pytest.fail('Must not tu be "Last_name" field')
