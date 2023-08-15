from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PageObjects.base_page import BasePage


class RegisterPage(BasePage):
    __url = "https://demo.guru99.com/test/newtours/register.php"
    __first_name_field =  (By.NAME, "firstName")
    __last_name_field = (By.NAME, "lastName")
    __phone_field = (By.NAME, "phone")
    __email_field = (By.NAME, "email")
    __address_field = (By.NAME, "address1")
    __city_field = (By.NAME, "city")
    __state_field = (By.NAME, "state")
    __postal_code_field = (By.NAME, "postalCode")
    __country_field = (By.NAME, "country")
    __username_field = (By.NAME, "userName")
    __password_field = (By.NAME, "password")
    __confirm_password_field = (By.NAME, "confirmPassword")
    __submit_btn = (By.NAME, "submit")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_register(
            self,
            first_name: str,
            last_name: str,
            phone: str,
            email: str,
            address: str,
            city: str,
            state: str,
            postal_code: str,
            country: str,
            username: str,
            password: str,
    ):
        super()._type(self.__first_name_field, first_name)
        super()._type(self.__last_name_field, last_name)
        super()._type(self.__phone_field, phone)
        super()._type(self.__email_field, email)
        super()._type(self.__address_field, address)
        super()._type(self.__city_field, city)
        super()._type(self.__state_field, state)
        super()._type(self.__postal_code_field, postal_code)
        super()._select(self.__country_field, country)
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._type(self.__confirm_password_field, password)
        super()._click(self.__submit_btn)
