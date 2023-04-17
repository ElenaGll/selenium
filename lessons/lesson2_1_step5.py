from selenium import webdriver
import time
import math


link = 'https://suninjuly.github.io/math.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    x_element = browser.find_element(by='id', value='input_value')
    x = x_element.text
    print(x_element, x)

    def calculate(value):
        return str(math.log(abs(12*math.sin(int(x)))))

    result = calculate(x)

    answer = browser.find_element(by='id', value='answer')
    answer.send_keys(result)

    check_robot = browser.find_element(by='css selector', value='[for="robotCheckbox"]')
    check_robot.click()

    radio_robot = browser.find_element(by='css selector', value='[for="robotsRule"]')
    radio_robot.click()

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(2)
