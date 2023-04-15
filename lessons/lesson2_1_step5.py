from selenium import webdriver
import time
import math


link = 'https://suninjuly.github.io/math.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    x_element = browser.find_element(by='id', value='input_value')
    x = x_element.text

    def calculate(value):
        return str(math.log(abs(12*math.sin(int(x)))))

    answer = calculate(x)
    time.sleep(2)

    input = browser.find_element(by='id', value='answer')
    input.send_keys(answer)
    time.sleep(1)

    check_robot = browser.find_element(by='css selector', value='[for="robotCheckbox"]')
    check_robot.click()
    time.sleep(1)

    radio_robot = browser.find_element(by='css selector', value='[for="robotsRule"]')
    radio_robot.click()
    time.sleep(1)

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(2)
