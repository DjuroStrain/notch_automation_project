import logging

from selenium.common import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import driver


logger = logging.getLogger(__name__)


class PageNavigation:
    @staticmethod
    def find_element(driver, *element):
        """
        Finds an element on a web page using the provided driver and element locator.

        This method waits for up to 10 seconds to locate the desired element and ensures
        that it is visible before returning it. If the element cannot be located within
        the timeout period or if it remains invisible, appropriate exceptions are raised.

        :param driver: WebDriver instance responsible for controlling the browser.
        :param element: The locator of the element to find. This can be a tuple containing
                        a By strategy (e.g., By.ID, By.CSS_SELECTOR) and the corresponding locator value.
        :return: The located WebElement.
        :raises TimeoutException: Raised if the element does not become visible within 10 seconds.
        """
        wait = WebDriverWait(driver, 10)
        try:
            return wait.until(EC.visibility_of_element_located(element))
        except TimeoutException:
            logger.error(f"Element with locator {element} not found on page.")
            return None

    @staticmethod
    def click_on_element(driver, *element):
        """
        Click on an element after waiting for it to become clickable.

        This method is a static utility designed to interact with web elements by
        waiting until they become clickable and then performing a click operation. It
        uses an explicit wait for up to 10 seconds to ensure the element is ready for
        interaction to prevent common timing issues.

        :param driver: WebDriver instance responsible for controlling the browser.
        :param element: The locator of the web element to wait for. This can be a tuple containing
                        a By strategy (e.g., By.ID, By.CSS_SELECTOR) and the corresponding locator value.
        :raises TimeoutException: Raised if the element does not become clickable within 10 seconds.
        """
        wait = WebDriverWait(driver, 10)
        try:
            wait.until(EC.element_to_be_clickable(element)).click()
        except TimeoutException:
            raise TimeoutException(f"Element with locator {element} not clickable within 10 seconds.")

    @staticmethod
    def input_text(driver, *element, text):
        """
        Provides functionality to input text into a specific web element after ensuring its visibility.

        :param driver: WebDriver instance responsible for controlling the browser.
        :param element: Locator of the web element. This can be a tuple containing
                        a By strategy (e.g., By.ID, By.CSS_SELECTOR) and the corresponding locator value.
        :param text: The string value to be input into the web element.
        """
        wait = WebDriverWait(driver, 10)
        try:
            wait.until(EC.visibility_of_element_located(element)).send_keys(text)
        except TimeoutException:
            raise TimeoutException(f"Element with locator {element} not visible within 10 seconds.")

    @staticmethod
    def select_option(driver, *element, option):
        """
        Selects an option from a dropdown menu, specified by its value, using a web
        driver to interact with the interface.

        :param driver: WebDriver instance responsible for controlling the browser.
        :param element: Locator of the select web element. This can be a tuple containing
                        a By strategy (e.g., By.ID, By.CSS_SELECTOR) and the corresponding locator value.
        :param option: The value attribute of the option to be selected.
        :return: None
        """
        select = Select(PageNavigation.find_element(driver, *element))
        select.select_by_value(option)

    @staticmethod
    def select_from_dropdown(driver, *element, option):
        """
        Selects an option from a dropdown or similar UI element by simulating click operations.

        This method performs two main actions:
        1. Clicks on the provided UI element to open the dropdown or selection menu.
        2. Locates and clicks on the desired option through its text representation.

        :param driver: WebDriver instance responsible for controlling the browser.
        :param element: Locator or reference to the UI element to be clicked to open the dropdown.
        :param option: The text value of the dropdown option to be selected.
        """
        PageNavigation.click_on_element(driver, *element)
        PageNavigation.click_on_element(driver, By.XPATH, f"//li[contains(text(), '{option}')]")