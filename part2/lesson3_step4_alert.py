# https://stepik.org/lesson/184253/step/4?unit=158843

import time
import math
from selenium import webdriver

link = 'https://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Firefox()
    browser.get(link)

    button_alert = browser.find_element_by_css_selector('button.btn')
    button_alert.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    x_elem = browser.find_element_by_id('input_value')
    x = x_elem.text
    answer = calc(x)

    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
