# https://stepik.org/lesson/165493/step/5?unit=140087

import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Firefox()
    browser.get('https://suninjuly.github.io/math.html')

    x_elem = browser.find_element_by_id('input_value')
    x = x_elem.text
    answer = calc(x)

    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(15)
    browser.quit()
