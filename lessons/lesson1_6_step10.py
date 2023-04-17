from selenium import webdriver
import time


link = 'http://suninjuly.github.io/registration1.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    first_name = browser.find_element(by='css selector', value='[placeholder="Input your first name"]')
    first_name.send_keys('Elena')

    last_name = browser.find_element(by='css selector', value='[placeholder="Input your last name"]')
    last_name.send_keys('Donyakina')

    email = browser.find_element(by='css selector', value='[placeholder="Input your email"]')
    email.send_keys('home@gmail.com')

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()

    welcome_text_elt = browser.find_element(by='tag name', value='h1')
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text
    time.sleep(2)
