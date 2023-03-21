from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_registration_page1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("test@test.com")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        self.assertEqual("Congratulations! You have successfully registered!", self.browser.find_element(By.TAG_NAME, "h1").text)

    def test_registration_page2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".first_block .form-control.third")))
        input2.send_keys("Petrov")
        input4 = self.browser.find_element(By.CSS_SELECTOR, ".form-control.second")
        input4.send_keys("Adress")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        self.assertEqual("Congratulations! You have successfully registered!", self.browser.find_element(By.TAG_NAME, "h1").text)


if __name__ == "__main__":
    unittest.main()