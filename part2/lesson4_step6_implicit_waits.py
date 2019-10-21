# https://stepik.org/lesson/181384/step/6?unit=156009

from selenium import webdriver

link = 'https://suninjuly.github.io/cats.html'

try:
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element_by_id("button")

finally:
    browser.quit()
