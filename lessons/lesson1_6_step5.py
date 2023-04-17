import time
from selenium import webdriver


link = 'http://suninjuly.github.io/find_link_text'

with webdriver.Chrome() as browser:
    browser.get(link)
    find_link = browser.find_element(by='link text', value='224592')
    find_link.click()

    first_name = browser.find_element(by='name', value='first_name')
    first_name.send_keys("Elena")
    last_name = browser.find_element(by='name', value='last_name')
    last_name.send_keys('Donyakina')
    city = browser.find_element(by='class name', value='city')
    city.send_keys("Moscow")
    country = browser.find_element(by='id', value='country')
    country.send_keys('Russia')

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(2)
