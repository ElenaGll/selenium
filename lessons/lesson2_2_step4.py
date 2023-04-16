from selenium import webdriver
import time


# with webdriver.Chrome() as browser:
#     browser.execute_script('document.title="Script executing"; alert("Robots at work!");')
#     time.sleep(3)

link = 'https://SunInJuly.github.io/execute_script.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element(by='tag name', value='button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()
    time.sleep(3)
