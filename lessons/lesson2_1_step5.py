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

    answer = calculate(x)
    time.sleep(0.5)

    input1 = browser.find_element(by='id', value='answer')
    input1.send_keys(answer)
    time.sleep(0.5)

    check_robot = browser.find_element(by='css selector', value='[for="robotCheckbox"]')
    check_robot.click()
    time.sleep(0.5)

    radio_robot = browser.find_element(by='css selector', value='[for="robotsRule"]')
    radio_robot.click()
    time.sleep(0.5)

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(1)
