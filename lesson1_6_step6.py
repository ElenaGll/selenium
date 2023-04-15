from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


EXE_PATH = r'..\chromedriver.exe'
opts = Options()

opts.add_experimental_option("excludeSwitches", ["enable-automation"])
opts.add_experimental_option('useAutomationExtension', False)

with webdriver.Chrome(chrome_options=opts, executable_path=EXE_PATH) as browser:
    # Переходим на страницу обот-пылесос на озон
    browser.get('https://www.ozon.ru/product/robot-pylesos-polaris-pvcr-1226-wi-fi-iq-home-gyro-chernyy-672452962/?avtc=1&avte=1&avts=1681564219&sh=T8DXMCUB5A')
    # Ищем "Добавить в корзину"
    add_button = browser.find_element(by='css selector', value='div.s5l div.aa1-a.sl4 div.s2l.x5-a.x5-f0 button.x5-a1.x5-f0')
    time.sleep(3)
    add_button.click()

    add_button = browser.find_element(by='css selector', value='a[href="/cart"]')
    add_button.click()

    time.sleep(15)
