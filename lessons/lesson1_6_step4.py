from selenium import webdriver
import time


link = 'http://suninjuly.github.io/simple_form_find_task.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    first_name = browser.find_element(by='name', value='first_name')
    first_name.send_keys('Elena')
    last_name = browser.find_element(by='name', value='last_name')
    last_name.send_keys('Donyakina')
    city = browser.find_element(by='class name', value='city')
    city.send_keys('Moscow')
    country = browser.find_element(by='id', value='country')
    country.send_keys("Russia")

    submit = browser.find_element(by='css selector', value='button.btn')
    submit.click()
    time.sleep(2)
