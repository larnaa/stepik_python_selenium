# https://stepik.org/lesson/138920/step/7?unit=196194

import time
from selenium import webdriver

try:
    browser = webdriver.Firefox()
    browser.get('http://suninjuly.github.io/huge_form.html')
    elements = browser.find_elements_by_css_selector('.first_block input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()