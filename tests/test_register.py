import time
import pytest

from PageObjects.register_page import RegisterPage
from PageObjects.successful_register_page import SuccessfulRegisterPage


class TestRegister:
    @pytest.mark.register
    def test_positive_register(self, driver):
        register_page = RegisterPage(driver)
        register_page.open()
        register_page.execute_register(
            "Alejo",
            "Perez",
            "351321321",
            "alejo@alejo.com",
            "San Martin 123",
            "Villa Allende",
            "Cordoba",
            "5000",
            "ARGENTINA",
            "alejoprueba",
            "alejoprueba"
        )
        time.sleep(2)

        successful_register_page = SuccessfulRegisterPage(driver)
        assert successful_register_page.expected_url == successful_register_page.current_url
        assert successful_register_page.is_logout_button_displayed()
