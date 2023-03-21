import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration_page1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("ivan@test.com")

        button = self.browser.find_element(By.XPATH, "//button[text()='Submit']")
        button.click()

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration_page2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("ivan@test.com")

        button = self.browser.find_element(By.XPATH, "//button[text()='Submit']")
        button.click()

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
