# https://stepik.org/lesson/138920/step/10?unit=196194

from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/registration1.html'
    # link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector('.first_block  .first_class input')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_css_selector('.first_block  .second_class input')
    last_name.send_keys('Petrov')
    email = browser.find_element_by_css_selector('.third_class input')
    email.send_keys('IP@mail.ru')
    phone = browser.find_element_by_css_selector('.second_block  .first_class input')
    phone.send_keys('80001112233')
    address = browser.find_element_by_css_selector('.second_block  .second_class input')
    address.send_keys('Russia')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
