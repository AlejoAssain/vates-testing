from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PageObjects.base_page import BasePage


class SuccessfulLoginPage(BasePage):
    __actual_url = "https://demo.guru99.com/test/newtours/login_sucess.php"
    __log_out_button = (By.LINK_TEXT, 'SIGN-OFF')
    __header = (By.TAG_NAME, "h3")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__actual_url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header)

    def is_expected_header(self):
        return self.header == "Login Successfully"

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__log_out_button)
