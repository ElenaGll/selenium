import os
from selenium import webdriver
import time


link = 'http://suninjuly.github.io/file_input.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    input_name = browser.find_element(by='name', value='firstname')
    input_name.send_keys('Elena')
    time.sleep(0.5)

    input_last_name = browser.find_element(by='name', value='lastname')
    input_last_name.send_keys('Donyakina')
    time.sleep(0.5)

    input_email = browser.find_element(by='name', value='email')
    input_email.send_keys('home@mail.com')
    time.sleep(0.5)

    current_dir = os.path.abspath(os.path.dirname('l2_2_s7.txt'))
    file_path = os.path.join(current_dir, 'l2_2_s7.txt')
    file = browser.find_element(by='name', value='file')
    file.send_keys(file_path)
    time.sleep(0.5)

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(5)

