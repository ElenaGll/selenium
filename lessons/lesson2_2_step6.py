from selenium import webdriver
import math
import time


link = 'https://SunInJuly.github.io/execute_script.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    value_x = browser.find_element(by='id', value='input_value')
    x = value_x.text

    def calculate(value):
        return str(math.log(abs(12*math.sin(int(value)))))

    result = calculate(x)
    time.sleep(0.5)

    answer = browser.find_element(by='id', value='answer')
    answer.send_keys(result)

    browser.execute_script("window.scrollBy(0, 200);")

    check_box = browser.find_element(by='id', value='robotCheckbox')
    check_box.click()
    time.sleep(0.5)

    radio_bottom = browser.find_element(by='id', value='robotsRule')
    radio_bottom.click()
    time.sleep(0.5)

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(5)
