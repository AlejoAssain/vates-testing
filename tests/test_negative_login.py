# Open browser
# selenium 4
import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.login_page import LoginPage
from PageObjects.unsuccessful_login_page import UnsuccessfulLoginPage


class TestNegativeLogin:
    @pytest.mark.login_negative
    def test_negative_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("incorrectUser", "Password123")
        time.sleep(3)

        unsuccessful_login_page = UnsuccessfulLoginPage(driver)
        assert unsuccessful_login_page.expected_url == unsuccessful_login_page.current_url
        assert unsuccessful_login_page.is_expected_error()

    @pytest.mark.login_negative
    def test_negative_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "incorrectPassword")
        time.sleep(3)

        unsuccessful_login_page = UnsuccessfulLoginPage(driver)
        assert unsuccessful_login_page.expected_url == unsuccessful_login_page.current_url
        assert unsuccessful_login_page.is_expected_error()
