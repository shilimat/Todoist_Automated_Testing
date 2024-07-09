import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from base_test import BaseTest

class CreateProjectTest(BaseTest):
    def test_create_project(self):
        self.login()
        try:
            time.sleep(4)
            # Step 1: Click the "My projects menu" button
            my_projects_menu_button = self.wait_for_element((By.ID, ":r1:"))
            my_projects_menu_button.click()
            
            # Step 2: Click the "Add project" button
            add_project_button = self.wait_for_element((By.XPATH, '//*[@aria-label="Add project"]'))
            add_project_button.click()
            
            # Fill in the project name
            project_name_field = self.wait_for_element((By.ID, 'edit_project_modal_field_name'))
            project_name_field.send_keys('New Project Name')
            
            # Select a project color
            color_dropdown_button = self.wait_for_element((By.CSS_SELECTOR, '[aria-labelledby="edit_project_modal_field_color_label"]'))
            color_dropdown_button.click()
            
            color_option = self.wait_for_element((By.XPATH, '//span[@style="background-color: var(--named-color-yellow);"]'))
            color_option.click()
            
            add_button = self.wait_for_element((By.XPATH, '//button[@type="submit" and contains(@class, "_8313bd46")]'))
            add_button.click()
            
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id=":r1v:"]')))

            print("Tase case 02: Project added successfully!")
            self.driver.quit()

        except TimeoutException as ex:
            self.fail(f"TimeoutException occurred: {ex}")
        except NoSuchWindowException as ex:
            self.fail(f"NoSuchWindowException occurred: {ex}")
        except NoSuchElementException as ex:
            self.fail(f"NoSuchElementException occurred: {ex}")
        except Exception as e:
            self.fail(f"Test Case: Create Project - Failed. Error: {e}")

if __name__ == "__main__":
    unittest.main()
    
