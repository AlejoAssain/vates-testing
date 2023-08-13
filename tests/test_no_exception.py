import time
import pytest

from PageObjects.exceptions_page import ExceptionPage


class TestSinExceptionPage:
    @pytest.mark.no_exception_page
    def test_no_such_element_exception_wait(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        time.sleep(1)
        assert exception_page.is_row_2_input_displayed()

    @pytest.mark.no_exception_page
    def test_element_not_interactive_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.send_keys_row_2()
        time.sleep(1)
        assert exception_page.confirmation_row_2()

    @pytest.mark.no_exception_page
    def test_invalid_element_state_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.clear_input()
        exception_page.send_keys_row_1()
        time.sleep(1)
        assert exception_page.confirmation_row_1()