from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PageObjects.base_page import BasePage


class SuccessfulRegisterPage(BasePage):
    __actual_url = "https://demo.guru99.com/test/newtours/register_sucess.php"
    __log_out_button = (By.LINK_TEXT, 'SIGN-OFF')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__actual_url

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__log_out_button)
