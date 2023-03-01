# Import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Define the website to navigate to
link = "https://suninjuly.github.io/math.html"

# Try to execute the following code block
try:
    # Create a new Chrome web driver instance
    browser = webdriver.Chrome()
    # Navigate to the website
    browser.get(link)

    import math

    def calc(x):
      return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x_element.text
    y = calc(x)

    # Find the input fields and fill in the required values

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input1.send_keys(y)

    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()

    # Click the submit button
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    # Wait for 5 seconds
    time.sleep(5)


# Finally, execute the following code block
finally:
    # Wait for 3 seconds
    time.sleep(3)
    # Close the web driver instance
    browser.quit()