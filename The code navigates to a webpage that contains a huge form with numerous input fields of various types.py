from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")

    for element in elements:
        random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
        element.send_keys(random_word)

    checkbox = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "input[value='robots']")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()