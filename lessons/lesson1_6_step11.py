from selenium import webdriver
import time


link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'

with webdriver.Chrome() as browser:
    browser.get(link1)
    time.sleep(2)

    input1 = browser.find_element(by='css selector', value='div.first_block input.form-control.first')
    input1.send_keys('Elena')

    input2 = browser.find_element(by='css selector', value='div.first_block input.form-control.second')
    input2.send_keys('Donyakina')

    input3 = browser.find_element(by='css selector', value='div.first_block input.form-control.third')
    input3.send_keys('home@gmail.com')

    button = browser.find_element(by='css selector', value='button.btn')
    button.click()
    time.sleep(3)

    welcome_text_elt = browser.find_element(by='tag name', value='h1')
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text
    time.sleep(2)
