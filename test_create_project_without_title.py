import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from base_test import BaseTest

class CreateProjectWithoutTitleTest(BaseTest):
    def test_create_project_without_title(self):
        self.login()
        try:
            time.sleep(4)
            # Step 1: Click the "My projects menu" button
            my_projects_menu_button = self.wait_for_element((By.ID, ":r1:"))
            my_projects_menu_button.click()
            
            # Step 2: Click the "Add project" button
            add_project_button = self.wait_for_element((By.XPATH, '//*[@aria-label="Add project"]'))
            add_project_button.click()

            add_button = self.wait_for_element((By.XPATH, '//button[@type="submit" and @aria-disabled="true" and contains(@class, "fb8d74bb")]/span[text()="Add"]/parent::button'))
            is_disabled = add_button.get_attribute("aria-disabled") == "true"
            if is_disabled:
                print("The button is disabled.")
                print("Test Case 03: Create Project Without Title - Passed")
            else:
                print("The button is enabled.")
                print("Test Case 03: Create Project Without Title - Failed")
                    
            
            
            
            self.driver.quit()

        except TimeoutException as ex:
            self.fail(f"TimeoutException occurred: {ex}")
        except NoSuchWindowException as ex:
            self.fail(f"NoSuchWindowException occurred: {ex}")
        except NoSuchElementException as ex:
            self.fail(f"NoSuchElementException occurred: {ex}")
        except Exception as e:
            self.fail(f"Test Case: Create Project Without Title - Failed. Error: {e}")

if __name__ == "__main__":
    unittest.main()
