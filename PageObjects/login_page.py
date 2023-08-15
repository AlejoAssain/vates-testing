from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PageObjects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://demo.guru99.com/test/newtours/index.php"
    __username_field = (By.NAME, "userName")
    __password_field = (By.NAME, "password")
    __submit_btn = (By.NAME, "submit")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_register(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_btn)
