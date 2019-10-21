# https://stepik.org/lesson/184253/step/5?unit=158843

import time
import math
from selenium import webdriver

link = 'https://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Firefox()
    browser.get(link)

    troll_button = browser.find_element_by_tag_name("button")
    troll_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
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
