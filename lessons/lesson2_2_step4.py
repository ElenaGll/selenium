from selenium import webdriver
import time


# with webdriver.Chrome() as browser:
#     browser.execute_script('document.title="Script executing"; alert("Robots at work!");')
#     time.sleep(3)

link = 'https://SunInJuly.github.io/execute_script.html'

with webdriver.Chrome() as browser:
    browser.get(link)

    submit = browser.find_element(by='tag name', value='button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', submit)
    submit.click()
    time.sleep(2)
