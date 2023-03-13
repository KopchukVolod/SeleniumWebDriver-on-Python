from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)


# Define the function to calculate the math expression
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    # find the two numbers to sum
    x = browser.find_element(By.CSS_SELECTOR, ".nowrap[id='input_value']")

    # get the text of the numbers and calculate the sum
    x_int = int(x.text)

    # Calculate the math expression
    y = calc(x_int)

    # Find the input field and fill in the required value
    input_field = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    time.sleep(3)

finally:
    # wait for a few seconds to ensure the page has loaded
    time.sleep(2)

    # close the browser
    browser.quit()
