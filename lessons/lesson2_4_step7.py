from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# Кнопка verify неактивна первую секунду после загрузке сайта
link = 'http://suninjuly.github.io/wait2.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    verify = WebDriverWait(browser, 5).until(
        expected_conditions.element_to_be_clickable((By.ID, 'verify'))
    )
    verify.click()

    verify_message = browser.find_element(by='id', value='verify_message')

    assert 'Verification was successful!' == verify_message.text
