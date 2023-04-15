from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/find_xpath_form'

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

    button = browser.find_element(by='xpath', value='//div[6]/button[3]')
    button.click()
    time.sleep(15)
