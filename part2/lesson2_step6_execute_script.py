# https://stepik.org/lesson/228249/step/6?unit=200781

import time
import math
from selenium import webdriver

link = 'https://suninjuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Firefox()
    browser.get(link)

    x_elem = browser.find_element_by_id('input_value')
    x = x_elem.text
    answer = calc(x)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
