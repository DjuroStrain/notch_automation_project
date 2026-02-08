from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class PageNavigation:
    @staticmethod
    def find_element(driver, *element):
        """
        Finds and returns a web element after waiting for its visibility within a specified timeout.

        The method waits for up to 10 seconds for the specified web element to become visible
        before returning it. If the element is not found within the timeout period or any
        exceptions occur during the process, the method safely returns None.

        :param driver: WebDriver instance responsible for controlling the browser.
        :param element: The locator of the web element to wait for. This can be a tuple containing
                        a By strategy (e.g., By.ID, By.CSS_SELECTOR) and the corresponding locator value.
        :return: The located web element if it becomes visible within the timeout period; otherwise, None.
        :rtype: WebElement | None
        """
        wait = WebDriverWait(driver, 10)
        try:
            return wait.until(EC.visibility_of_element_located(element))
        except NoSuchElementException:
            return None
        except TimeoutException:
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
        """
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(element)).click()

    @staticmethod
    def input_text(driver, *element, text):
        """
        Provides functionality to input text into a specific web element after ensuring its visibility.

        :param driver: WebDriver instance responsible for controlling the browser.
        :param element: Locator of the web element (tuple consisting of locator strategy and value).
        :param text: The string value to be input into the web element.
        """
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(element)).send_keys(text)

    @staticmethod
    def select_option(driver, *element, option):
        """
        Selects an option from a dropdown menu, specified by its value, using a web
        driver to interact with the interface.

        :param driver: WebDriver instance responsible for controlling the browser.
        :param element: Locator strategy and locator for identifying the select element.
        :param option: The value attribute of the option to be selected.
        :return: None
        """
        select = Select(driver.find_element(*element))
        select.select_by_value(option)

    # @staticmethod
    # def select_option(driver, *element, option):
    #     """
    #     Selects an option from a dropdown or similar UI element by simulating click operations.
    #
    #     This method performs two main actions:
    #     1. Clicks on the provided UI element to open the dropdown or selection menu.
    #     2. Locates and clicks on the desired option through its text representation.
    #
    #     :param driver: WebDriver instance responsible for controlling the browser.
    #     :param element: Locator or reference to the UI element to be clicked to open the selection options.
    #     :param option: The text value of the option to be selected.
    #     """
    #     PageNavigation.click_on_element(driver, *element)
    #     PageNavigation.click_on_element(driver, By.XPATH, f"//li[contains(text(), '{option}')]")