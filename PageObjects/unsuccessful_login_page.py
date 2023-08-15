from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PageObjects.base_page import BasePage


class UnsuccessfulLoginPage(BasePage):
    __actual_url = "https://demo.guru99.com/test/newtours/index.php"
    __error_message = (By.TAG_NAME, "span")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__actual_url

    @property
    def error_message(self) -> str:
        return super()._get_text(self.__error_message)

    def is_expected_error_message(self):
        return self.error_message == "Enter your userName and password correct"
