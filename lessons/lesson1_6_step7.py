from selenium import webdriver
import time

link = 'http://suninjuly.github.io/huge_form.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    elements = browser.find_elements(by='tag name', value='input')

    for element in elements:
        element.send_keys('answer')

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()

    time.sleep(2)
