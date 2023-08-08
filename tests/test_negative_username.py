# Open browser
# selenium 4
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestNegativeScenariosUn:
    @pytest.mark.login
    def test_negative_username(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        time.sleep(3)
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)
        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")
        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        # Push Submit button

        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(5)
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed"
        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"
