import pytest
from selenium import webdriver


@pytest.fixture(params="chrome")
def driver(request):
    browser = request.param
    print(f"Creating {browser} driver ")

    if browser == "chrome":
        driver = webdriver.Chrome()
        yield driver

    elif browser == "Firefox":
        driver = webdriver.Firefox()
        yield driver

    print(f"Closing {browser} driver")
    driver.quit()
