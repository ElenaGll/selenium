from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link1 = 'https://suninjuly.github.io/selects1.html'
link2 = 'https://suninjuly.github.io/selects2.html'

with webdriver.Chrome() as browser:
    browser.get(link1)

    num1 = browser.find_element(by='id', value='num1')
    num2 = browser.find_element(by='id', value='num2')
    one = num1.text
    two = num2.text
    result = str(int(one) + int(two))

    select = Select(browser.find_element(by='tag name', value='select'))
    select.select_by_value(result)

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(2)
