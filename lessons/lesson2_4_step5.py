from selenium import webdriver


link = 'http://suninjuly.github.io/wait1.html'

with webdriver.Chrome() as browser:
    # # webdriver будет искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get(link)

    verify = browser.find_element(by='id', value='verify')
    verify.click()

    verify_message = browser.find_element(by='id', value='verify_message')

    assert 'Verification was successful!' == verify_message.text
