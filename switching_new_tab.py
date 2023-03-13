from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)


# Define the function to calculate the math expression
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    # To find out the name of a new tab, you need to use the window_handles method, which returns an array of names of all tabs.
    # Knowing that two tabs are now open in the browser, select the second tab:
    # new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # To switch to a new tab, it is necessary to clearly indicate which tab we want to switch to.
    # This is done using the switch_to.window command:

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
    time.sleep(3)

    # close the browser
    browser.quit()
