import pytest
from selenium import webdriver



@pytest.fixture(scope='function')
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()
