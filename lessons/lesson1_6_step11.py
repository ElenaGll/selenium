from selenium import webdriver
import time


class RegisterForm:
    def __init__(self, link):
        self.link = link

    def get_welcome_text(self):
        with webdriver.Chrome() as browser:
            browser.get(self.link)

            first_name = browser.find_element(by='css selector', value='div.first_block input.form-control.first')
            first_name.send_keys('Elena')

            last_name = browser.find_element(by='css selector', value='div.first_block input.form-control.second')
            last_name.send_keys('Donyakina')

            email = browser.find_element(by='css selector', value='div.first_block input.form-control.third')
            email.send_keys('home@gmail.com')

            submit = browser.find_element(by='css selector', value='button.btn')
            submit.click()
            time.sleep(1)

            welcome_text_elt = browser.find_element(by='tag name', value='h1')
            welcome_text = welcome_text_elt.text

            return welcome_text
