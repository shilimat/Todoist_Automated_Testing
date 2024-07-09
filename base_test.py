# base_test.py
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://app.todoist.com")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        try:
            self.driver.quit()
        except NoSuchWindowException:
            print("Browser window already closed.")

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def login(self):
        try:
           
            # Fill in the email and password fields
            email_input = self.wait_for_element((By.ID, "element-0"))
            email_input.clear()
            email_input.send_keys("shilimattadele@gmail.com")

            password_input = self.wait_for_element((By.ID, "element-3"))
            password_input.clear()
            password_input.send_keys("Ilovecody@2001")

            time.sleep(1)  # Wait for 1 second

            # Submit the form
            password_input.send_keys(Keys.RETURN)
            # Wait for the page to load after login
            self.wait_for_element((By.CSS_SELECTOR, "button.plus_add_button"))
        except Exception as e:
            print(f"Login failed. Error: {e}")
            self.fail("Login failed")
