import os
from selenium import webdriver
import time


link = 'http://suninjuly.github.io/file_input.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    first_name = browser.find_element(by='name', value='firstname')
    first_name.send_keys('Elena')

    last_name = browser.find_element(by='name', value='lastname')
    last_name.send_keys('Donyakina')

    email = browser.find_element(by='name', value='email')
    email.send_keys('home@mail.com')

    current_dir = os.path.abspath(os.path.dirname('l2_2_s7.txt'))
    file_path = os.path.join(current_dir, 'l2_2_s7.txt')
    file = browser.find_element(by='name', value='file')
    file.send_keys(file_path)

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(2)

