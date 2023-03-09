from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/selects1.html"
browser.get(link)

try:
    # find the two numbers to sum
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")

    # get the text of the numbers and calculate the sum
    sum = int(num1.text) + int(num2.text)

    # select the sum value from the dropdown list
    select = browser.find_element(By.TAG_NAME, "select")
    option = select.find_element(By.CSS_SELECTOR, f"option[value='{sum}']")
    option.click()

    # click the Submit button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # wait for a few seconds to ensure the page has loaded
    time.sleep(5)

    # close the browser
    browser.quit()