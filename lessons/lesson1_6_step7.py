from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/huge_form.html'

with webdriver.Chrome() as browser:
    browser.get(link)
    time.sleep(3)

    elements = browser.find_elements(by='tag name', value='input')

    for element in elements:
        element.send_keys('answer')

    button = browser.find_element(by='css selector', value='button.btn')
    button.click()

    time.sleep(15)
