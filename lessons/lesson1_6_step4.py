from selenium import webdriver
import time


link = 'http://suninjuly.github.io/simple_form_find_task.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    input1 = browser.find_element(by='name', value='first_name')
    input1.send_keys('Elena')
    input2 = browser.find_element(by='name', value='last_name')
    input2.send_keys('Donyakina')
    input3 = browser.find_element(by='class name', value='city')
    input3.send_keys('Moscow')
    input4 = browser.find_element(by='id', value='country')
    input4.send_keys("Russia")

    button = browser.find_element(by='css selector', value='button.btn')
    button.click()
    time.sleep(10)
