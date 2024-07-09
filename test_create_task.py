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

class CreateTaskTest(BaseTest):
    def test_create_task(self):
        self.login()
        try:
            time.sleep(4)
            # Step 1: Click the "My Task menu" button
            my_task_button = self.wait_for_element((By.XPATH, '//button[@type="button" and contains(@class, "vZhNClH") and contains(@class, "_8313bd46")]'))
            my_task_button.click()
            
            # Step 2: Click the "Add Task" button
            task_element = self.wait_for_element((By.XPATH, '//p[@data-placeholder="Task name" and contains(@class, "is-empty") and contains(@class, "is-editor-empty")]'))
            task_element.click()
            task_element.send_keys("New Task")
            
            add_task_button = self.wait_for_element((By.XPATH, '//button[@data-testid="task-editor-submit-button"]'))
            add_task_button.click()
            
            print("Test Case 04: Create Task - Passed")

        except TimeoutException as ex:
            self.fail(f"TimeoutException occurred: {ex}")
        except NoSuchWindowException as ex:
            self.fail(f"NoSuchWindowException occurred: {ex}")
        except NoSuchElementException as ex:
            self.fail(f"NoSuchElementException occurred: {ex}")
        except Exception as e:
            self.fail(f"Test Case: Create Task - Failed. Error: {e}")

if __name__ == "__main__":
    unittest.main()
