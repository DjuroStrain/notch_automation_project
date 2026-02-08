import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("driver")
class BaseTest:
    driver: WebDriver