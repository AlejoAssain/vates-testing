from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PageObjects.base_page import BasePage


class UnsuccessfulLoginPage(BasePage):
    __actual_url = "https://practicetestautomation.com/practice-test-login/"
    __error = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__actual_url

    @property
    def error(self) -> str:
        return super()._get_text(self.__error)

    def is_expected_error(self):
        return self.error == "Your username is invalid!" or self.error == "Your password is invalid!"
