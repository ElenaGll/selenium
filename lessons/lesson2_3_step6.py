from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/redirect_accept.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    submit1 = browser.find_element(by='css selector', value='button.trollface.btn')
    submit1.click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(second_window)

    value_x = browser.find_element(by='id', value='input_value')
    x = value_x.text

    def calculate(value):
        return str(math.log(abs(12*math.sin(int(value)))))

    result = calculate(x)

    answer = browser.find_element(by='id', value='answer')
    answer.send_keys(result)

    submit2 = browser.find_element(by='css selector', value='button.btn')
    submit2.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(2)
