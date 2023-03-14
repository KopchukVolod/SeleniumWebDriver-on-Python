from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Wait for the price of the house to decrease to $100
wait = WebDriverWait(browser, 12)
price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

# Click on the "Book" button
book_btn = browser.find_element(By.ID, "book")
book_btn.click()

# Solve the math problem
x = int(browser.find_element(By.ID, "input_value").text)
answer = str(math.log(abs(12*math.sin(x))))
answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(answer)
submit_btn = browser.find_element(By.CSS_SELECTOR, "button[id='solve']")
submit_btn.click()

# Get the result from the alert window
alert = browser.switch_to.alert
result = alert.text.split()[-1]
alert.accept()
print(result)

# Close the browser
browser.quit()
