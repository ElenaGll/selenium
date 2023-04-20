import pytest
from selenium import webdriver


@pytest.mark.parametrize('language', ['ru', 'en-gb'])
def test_guest_should_see_login_link(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/'
    browser.get(link)
    browser.find_element(by='css selector', value='#login_link')
