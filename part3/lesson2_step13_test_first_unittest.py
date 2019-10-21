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

        first_name = browser.find_element_by_css_selector('.first_block .first')
        first_name.send_keys('Kesa')
        last_name = browser.find_element_by_css_selector('.first_block .second')
        last_name.send_keys('Lisa')
        email = browser.find_element_by_css_selector('.third_class .third')
        email.send_keys('KL@google.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(2)

        welcome_text = browser.find_element_by_tag_name('h1')
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text.text)

    def test_registration_bug(self):
        browser = self.driver
        browser.get(link_bug_page)

        first_name = browser.find_element_by_css_selector('.first_block .first')
        first_name.send_keys('Kesa')
        last_name = browser.find_element_by_css_selector('.first_block .second')
        last_name.send_keys('Lisa')
        email = browser.find_element_by_css_selector('.third_class .third')
        email.send_keys('KL@google.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(2)

        welcome_text = browser.find_element_by_tag_name('h1')
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
