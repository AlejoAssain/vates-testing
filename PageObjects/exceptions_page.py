import time

from PageObjects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ExceptionPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row_2_input_locator = (By.ID, "row2")
    __field_input_locator_2 = (By.XPATH, "(//input[contains(@type,'text')])[2]")
    __save_btn_locator_2 = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __save_btn_locator_1 = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __field_input_locator = (By.XPATH, '//*[@id="row1"]/input')
    __input_text = "Pasta"
    __confirmation_locator = (By.ID, "confirmation")
    __edit_btn_locator = (By.XPATH, "//button[contains(@id,'edit_btn')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row_2_input_locator, 10)

    def is_row_2_input_displayed(self):
        return super()._is_displayed(self.__row_2_input_locator)

    def send_keys_row_2(self):
        super()._type(self.__field_input_locator_2, self.__input_text)
        super()._click(self.__save_btn_locator_2)

    def send_keys_row_1(self):
        super()._type(self.__field_input_locator, self.__input_text)
        super()._click(self.__save_btn_locator_1)

    def confirmation_row_2(self):
        return super()._is_displayed(self.__confirmation_locator)

    def clear_input(self):
        super()._click(self.__edit_btn_locator)
        super()._wait_until_element_is_clickable(self.__field_input_locator)
        super()._clear(self.__field_input_locator)

    def confirmation_row_1(self):
        return super()._is_displayed(self.__confirmation_locator)