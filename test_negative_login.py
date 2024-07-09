import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from base_test import BaseTest

class LoginNegativeTest(BaseTest):
    def test_negative_login(self):
        
        email_input = self.wait_for_element((By.ID, "element-0"))
        email_input.clear()
        email_input.send_keys("shilimattadele@gmail.com")

        password_input = self.wait_for_element((By.ID, "element-3"))
        password_input.clear()
        password_input.send_keys("abcdetetetetete")
        password_input.send_keys(Keys.RETURN)
            # Wait for the page to load after login
        add_button = self.wait_for_element((By.CSS_SELECTOR, "button.plus_add_button"))
        add_button.click()

        error_message = self.wait_for_element((By.XPATH, '//div[@class="a83bd4e0 _266d6623 _8f5b5f2b fb8d74bb"]'))

        if "Wrong email or password" in error_message.text:
            print("Test passed: The error message is displayed.")
        else:
            print("Test failed: The error message is not displayed.")

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
