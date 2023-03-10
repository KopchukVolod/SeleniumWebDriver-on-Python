# Job on execute_script. In this task, you will have to overcome the captcha for robots again and deal with the terrible and huge footer, which the designer still has no time to remake. You will need to write code to:
#Open https://SunInJuly.github.io/execute_script.html page .
# Read value for variable x.
# Calculate the mathematical function of x.
# Scroll down the page.
# Enter your answer in the text field.
# Select checkbox "I'm the robot".
# Toggle radiobutton "Robots rule!".
# Click on the "Submit" button.
# If everything is done correctly and fast enough (this task also has a time limit), you will see a window with a number. Submit the resulting number as an answer for this assignment.

# For this task, you will need to use the execute_script method to scroll into the viewport of the elements that are overlaid by the footer.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)


# Define the function to calculate the math expression
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # find the two numbers to sum
    x = browser.find_element(By.CSS_SELECTOR, ".nowrap[id='input_value']")

    # get the text of the numbers and calculate the sum
    x_int = int(x.text)

    # Calculate the math expression
    y = calc(x_int)

    #browser.execute_script("window.scrollBy(0, 150);")

    # Find the input field and fill in the required value
    input_field = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input_field.send_keys(y)

    browser.execute_script("window.scrollBy(0, 150);")

    # Find the checkbox and select it
    checkbox = browser.find_element(By.CSS_SELECTOR, ".form-check-input[type='checkbox']")
    checkbox.click()
    time.sleep(1)

    # Find the radiobutton and select it
    radiobutton = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotsRule")
    radiobutton.click()
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    time.sleep(3)

finally:
    # wait for a few seconds to ensure the page has loaded
    time.sleep(5)

    # close the browser
    browser.quit()
