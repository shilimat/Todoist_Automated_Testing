import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from base_test import BaseTest

class LoginTest(BaseTest):
    def test_login(self):
        self.login()        
        my_projects_menu_button = self.wait_for_element((By.ID, ":r1:"))
        if my_projects_menu_button:
            print("Test Case 01: Login to Todoist - Passed")
        else:
            print("Test Case 01: Login to Todoist - Failed")

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
