import time
import pytest

from PageObjects.login_page import LoginPage
from PageObjects.successful_login_page import SuccessfulLoginPage
from PageObjects.unsuccessful_login_page import UnsuccessfulLoginPage


class TestLogin:
    @pytest.mark.login
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_register("alejo@alejo.com", "alejoprueba")
        time.sleep(2)

        successful_login_page = SuccessfulLoginPage(driver)
        assert successful_login_page.expected_url == successful_login_page.current_url
        assert successful_login_page.is_expected_header()
        assert successful_login_page.is_logout_button_displayed()

    @pytest.mark.login
    def test_negative_password_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_register("alejo@alejo.com", "incorrectPassword")
        time.sleep(2)

        unsuccessful_login_page = UnsuccessfulLoginPage(driver)
        assert unsuccessful_login_page.expected_url == unsuccessful_login_page.current_url
        assert unsuccessful_login_page.is_expected_error_message()

    @pytest.mark.login
    def test_negative_username_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_register("incorrectUsername@incorrect.com", "alejoprueba")
        time.sleep(2)

        unsuccessful_login_page = UnsuccessfulLoginPage(driver)
        assert unsuccessful_login_page.expected_url == unsuccessful_login_page.current_url
        assert unsuccessful_login_page.is_expected_error_message()
