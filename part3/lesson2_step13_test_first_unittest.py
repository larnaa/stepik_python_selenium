# https://stepik.org/lesson/36285/step/13?unit=162401

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class TestUniqueSelectors(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def fill_form(self, link):
        browser = self.driver
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kesa')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Lisa')
        browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(2)

        welcome_text = browser.find_element_by_tag_name('h1')
        return welcome_text.text

    def test_registration(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_bug(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
