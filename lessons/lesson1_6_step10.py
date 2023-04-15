from selenium import webdriver
import time


link = 'http://suninjuly.github.io/registration1.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    time.sleep(2)

    input1 = browser.find_element(by='css selector', value='[placeholder="Input your first name"]')
    input1.send_keys('Elena')

    input2 = browser.find_element(by='css selector', value='[placeholder="Input your last name"]')
    input2.send_keys('Donyakina')

    input3 = browser.find_element(by='css selector', value='[placeholder="Input your email"]')
    input3.send_keys('home@gmail.com')

    button = browser.find_element(by='css selector', value='button.btn')
    button.click()
    time.sleep(3)

    welcome_text_elt = browser.find_element(by='tag name', value='h1')
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text
    time.sleep(2)
