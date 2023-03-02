from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(5)

    # If we want to find an element by the full match of the text, then the following code will suit us:
    link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    # Find the input fields and fill in the required values
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Volodymyr")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Kopchuk")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Zhytomyr")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Ukraine")

 # Click the submit button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()