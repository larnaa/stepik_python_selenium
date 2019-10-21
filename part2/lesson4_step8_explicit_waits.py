# https://stepik.org/lesson/181384/step/8?unit=156009

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Firefox()
    browser.get(link)

    house_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    button_book = browser.find_element(By.ID, 'book').click()

    x_elem = browser.find_element(By.ID, 'input_value')
    x = x_elem.text
    answer = calc(x)
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)

    button_submit = browser.find_element(By.ID, 'solve')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
