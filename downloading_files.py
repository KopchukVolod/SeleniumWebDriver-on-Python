#Importing required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

#Initializing the browser instance
browser = webdriver.Chrome()
#Storing the URL to navigate to
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

#Finding the current directory and defining the file path
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')

try:

    # Find the input fields and fill in the required values
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Volodymyr")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Kopchuk")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input3.send_keys("kop@gmail.com")


    # Finding the element to upload a file and sending the file path
    element4 = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    element4.send_keys(file_path)

    # Finding the submit button and clicking it
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    
    # Adding sleep time to wait for the page to load
    time.sleep(3)

finally:
    # wait for a few seconds to ensure the page has loaded
    time.sleep(5)

    # close the browser
    browser.quit()


