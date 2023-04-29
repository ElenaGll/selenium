import allure
import pytest


link = 'http://selenium1py.pythonanywhere.com/'


@allure.feature('Stepik test')
@allure.story('Guest should see different options')
class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        with allure.step('See login link'):
            browser.find_element(by='id', value='login_link')

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        with allure.step('See basket link'):
            browser.find_element(by='css selector', value='.basket-mini .btn-group > a')

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        with allure.step('See search button'):
            browser.find_element(by='css selector', value='input.btn.btn-default')
