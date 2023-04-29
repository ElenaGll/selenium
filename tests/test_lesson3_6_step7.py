import pytest

link = 'http://selenium1py.pythonanywhere.com/'

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    assert browser.find_element(by='css selector', value='#login_link')

@pytest.mark.xfail
def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    assert browser.find_element(by='css selector', value='#magic_link')
