# https://stepik.org/lesson/228249/step/8?unit=200781

import time
import os
from selenium import webdriver

link = 'https://suninjuly.github.io/file_input.html'


try:
    browser = webdriver.Firefox()
    browser.get(link)

    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Kesa')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Lisa')

    email = browser.find_element_by_name('email')
    email.send_keys('KL@google.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path: str = os.path.join(current_dir, 'bio.txt')

    with open(file=file_path, mode='w') as file:
        file.write('Kes')

    browse_button = browser.find_element_by_name('file')
    browse_button.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

    os.remove(file_path)

finally:
    time.sleep(10)
    browser.quit()
