# https://stepik.org/lesson/36285/step/13?unit=162401

import unittest
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration1.html'
link_bug_page = 'http://suninjuly.github.io/registration2.html'


class TestUniqueSelectors(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_registration(self):
        browser = self.driver
        browser.get(link)

    def test_registration_bug(self):
        browser = self.driver
        browser.get(link_bug_page)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


'''
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
'''