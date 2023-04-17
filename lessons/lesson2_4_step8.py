from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import math
import time


link = 'http://suninjuly.github.io/explicit_wait2.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    book = browser.find_element(by='id', value='book')
    WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book.click()

    value_x = browser.find_element(by='id', value='input_value')
    x = value_x.text

    def calculate(value):
        return str(math.log(abs(12 * math.sin(int(value)))))

    result = calculate(x)

    answer = browser.find_element(by='id', value='answer')
    answer.send_keys(result)

    submit = browser.find_element(by='id', value='solve')
    submit.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(2)
