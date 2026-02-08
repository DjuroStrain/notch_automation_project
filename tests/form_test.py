import time
from logging import Logger

import allure
import pytest
from selenium.common import TimeoutException
from helpers.page_navigation import PageNavigation
from pages.form_page import FormPage
from test_data.test_data import TestData
from test_data.test_locators import TestLocators
from tests.base_test import BaseTest
import pytest_check as check


page_nav = PageNavigation()


class TestForm(BaseTest):
    @pytest.fixture(autouse=True)
    def before_each_test(self):
        try:
            page_nav.click_on_element(self.driver, *TestLocators.accept_all_cookies_btn)
        except TimeoutException as e:
            Logger.warning(f"Timeout occurred: " + str(e))
            pass

    @allure.title("Test form components visibility")
    @allure.description("Verify that all form components are visible")
    def test_mandatory_form_components(self):
        form_page = FormPage(self.driver)
        form_elements = form_page.form_mandatory_components()
        self.driver.save_screenshot("screenshot.png")
        for locator, name in form_elements:
            el = page_nav.find_element(self.driver, *locator)
            check.is_true(el, f"{name} is visible")

    @allure.title("Test form submit - mandatory fields")
    @allure.description("Verify that form can be submitted with mandatory fields filled")
    def test_form_submit_mandatory_fields(self):
        form_page = FormPage(self.driver)
        form_page.fill_mandatory_fields(TestData.UserData.mandatory_user_data)
        form_page.check_privacy_policy()
        form_page.submit_form()
        assert form_page.get_confirmation_message() == TestData.confirmation_msg

    @allure.title("Test form submit - all fields")
    @allure.description("Verify that form can be submitted with all fields filled")
    def test_form_submit_all_fields(self):
        form_page = FormPage(self.driver)
        form_page.fill_all_fields(TestData.UserData.complete_user_data)
        form_page.check_privacy_policy()
        form_page.submit_form()
        assert form_page.get_confirmation_message() == TestData.confirmation_msg

    @allure.title("Test form submit - invalid email")
    @allure.description("Verify that form cannot be submitted with invalid email")
    def test_form_submit_invalid_email(self):
        form_page = FormPage(self.driver)
        form_page.submit_with_invalid_email(TestData.UserData.user_data_invalid_email)
        form_page.check_privacy_policy()
        form_page.submit_form()
        assert form_page.get_invalid_email_message() == TestData.invalid_email_msg
        time.sleep(5)

    @allure.title("Test form submit - missing mandatory fields")
    @allure.description("Verify that form cannot be submitted with missing mandatory fields")
    def test_form_submit_missing_mandatory_fields(self):
        form_page = FormPage(self.driver)
        form_page.submit_form()
        validation_messages = form_page.validation_messages()
        for locator, msg in validation_messages:
            check.equal(page_nav.find_element(self.driver, *locator).text, TestData.missing_mandatory_fields_msg, msg)
        time.sleep(5)
