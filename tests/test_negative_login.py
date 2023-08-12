# Open browser
# selenium 4
import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeLogin:
    @pytest.mark.login
    def test_negative_username(self, driver):
        pass

    @pytest.mark.login
    def test_negative_password(self, driver):
        pass
