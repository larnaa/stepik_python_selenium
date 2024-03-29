# https://stepik.org/lesson/138920/step/8?unit=196194

import time
from selenium import webdriver

try:
    browser = webdriver.Firefox()
    browser.get('http://suninjuly.github.io/find_xpath_form')

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(15)
    browser.quit()
