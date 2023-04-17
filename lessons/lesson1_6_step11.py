from selenium import webdriver
import time


link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html' # Raise error 'NoSuchElementException

with webdriver.Chrome() as browser:
    browser.get(link1)

    first_name = browser.find_element(by='css selector', value='div.first_block input.form-control.first')
    first_name.send_keys('Elena')

    last_name = browser.find_element(by='css selector', value='div.first_block input.form-control.second')
    last_name.send_keys('Donyakina')

    email = browser.find_element(by='css selector', value='div.first_block input.form-control.third')
    email.send_keys('home@gmail.com')

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()

    welcome_text_elt = browser.find_element(by='tag name', value='h1')
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text
    time.sleep(2)
