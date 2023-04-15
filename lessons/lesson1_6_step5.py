import time
from selenium import webdriver


link = 'http://suninjuly.github.io/find_link_text'

with webdriver.Chrome() as browser:
    browser.get(link)
    find_link = browser.find_element(by='link text', value='224592')
    find_link.click()

    input1 = browser.find_element(by='name', value='first_name')
    input1.send_keys("Elena")
    input2 = browser.find_element(by='name', value='last_name')
    input2.send_keys('Donyakina')
    input3 = browser.find_element(by='class name', value='city')
    input3.send_keys("Moscow")
    input4 = browser.find_element(by='id', value='country')
    input4.send_keys('Russia')

    button = browser.find_element(by='css selector', value='button.btn')
    button.click()
    time.sleep(10)

    time.sleep(5)
