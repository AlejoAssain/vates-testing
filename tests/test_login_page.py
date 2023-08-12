import time
import pytest

from PageObjects.login_page import LoginPage
from PageObjects.successful_login_page import SuccessfulLoginPage


class TestPositiveScenarios:
    @pytest.mark.login
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        time.sleep(3)

        successful_login_page = SuccessfulLoginPage(driver)
        assert successful_login_page.expected_url == successful_login_page.current_url
        assert successful_login_page.is_expected_header()
        assert successful_login_page.is_logout_button_displayed()
