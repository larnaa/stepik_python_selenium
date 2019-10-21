# https://stepik.org/lesson/228249/step/3?unit=200781

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Firefox()
    browser.get(link)

    number_1 = browser.find_element_by_id('num1')
    number_2 = browser.find_element_by_id('num2')
    summ = int(number_1.text) + int(number_2.text)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
