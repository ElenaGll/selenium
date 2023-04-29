import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(3)

    assert browser.find_element(by='css selector', value='button.btn-add-to-basket')
