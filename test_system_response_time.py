# test_create_task.py
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from base_test import BaseTest

class SystemResponseTimeTest(BaseTest):
    def test_system_response_time(self):
        
        
        
        element_selector = (By.ID, "element-0")
        max_allowed_time = 2

        try:
            
            self.setUp()
            start_time = time.time()            
            self.wait_for_element(element_selector)            
            end_time = time.time()
            response_time = end_time - start_time


            if (response_time <= max_allowed_time):
                print("Loading exceeds the maximum allowed time of 2 seconds.")
                print("Test Case 15: System Response Time - Failed")
            else:
                print("Test Case 15: System Response Time - Passed")
               
           

        except Exception as e:
            self.fail(f"Test Case 15: Failed. Error {e}")

if __name__ == "__main__":
    unittest.main()
