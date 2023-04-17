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

    result = calculate(value_x)

    answer = browser.find_element(by='id', value='answer')
    answer.send_keys(result)

    check_robot = browser.find_element(by='id', value='robotCheckbox')
    check_robot.click()

    radio_robot = browser.find_element(by='id', value='robotsRule')
    radio_robot.click()

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(2)
