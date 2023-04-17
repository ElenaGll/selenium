import time
from selenium import webdriver


link = 'https://suninjuly.github.io/text_input_task.html'

# Конструкция with .. as гарантирует, что браузер будет закрыт вне зависимости
# от того, что введёт пользователь (чтобы не использовать browser.quit())
with webdriver.Chrome() as browser:
    time.sleep(3)
    browser.get(link)

    # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему
    # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
    # Ищем поле для ввода текста
    textarea = browser.find_element(by='css selector', value='.textarea')

    # Напишем текст ответа в найденное поле
    textarea.send_keys('get()')

    # Найдем кнопку, которая отправляет введенное решение
    submit = browser.find_element(by='css selector', value='.submit-submission')
    # Скажем драйверу, что нужно нажать на кнопку
    submit.click()
    time.sleep(2)
