from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/get_attribute.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    treasure_box = browser.find_element(by='id', value='treasure')
    value_x = treasure_box.get_attribute('valuex')

    def calculate(value):
        return str(math.log(abs(12*math.sin(int(value)))))

    answer = calculate(value_x)
    time.sleep(0.5)

    input1 = browser.find_element(by='id', value='answer')
    input1.send_keys(answer)
    time.sleep(0.5)

    check_robot = browser.find_element(by='id', value='robotCheckbox')
    check_robot.click()
    time.sleep(0.5)

    radio_robot = browser.find_element(by='id', value='robotsRule')
    radio_robot.click()
    time.sleep(0.5)

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(2)
