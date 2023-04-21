import allure
import pytest
from selenium import webdriver


@allure.feature('Stepik test')
@allure.story('Guest should see  login link on en and ru version of website')
@pytest.mark.parametrize('language', ['ru', 'en-gb'])
def test_guest_should_see_login_link(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/'
    browser.get(link)
    with allure.step('See login link'):
        browser.find_element(by='css selector', value='#login_link')
