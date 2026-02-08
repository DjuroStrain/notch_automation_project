from selenium.webdriver.common.by import By
from helpers.page_navigation import PageNavigation
from test_data.test_locators import TestLocators


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def form_mandatory_components():
        return [
            (TestLocators.Form.first_name_input, "First name input"),
            (TestLocators.Form.last_name_input, "Last name input"),
            (TestLocators.Form.email_input, "Email input"),
            (TestLocators.Form.needed_services_container, "Needed services container"),
            (TestLocators.Form.privacy_policy_checkbox, "Privacy policy checkbox"),
            (TestLocators.Form.send_msg_btn, "Send message button"),
        ]

    @staticmethod
    def validation_messages():
        return [
            (TestLocators.Form.first_name_validation_msg, "First name validation message"),
            (TestLocators.Form.last_name_validation_msg, "Last name validation message"),
            (TestLocators.Form.email_validation_msg, "Email validation message"),
            (TestLocators.Form.needed_services_validation_msg, "Needed services validation message"),
            (TestLocators.Form.privacy_policy_checkbox_validation_msg, "Privacy policy checkbox validation message")
        ]

    def input_first_name(self, first_name: str):
        PageNavigation.input_text(self.driver, *TestLocators.Form.first_name_input, text=first_name)

    def input_last_name(self, last_name: str):
        PageNavigation.input_text(self.driver, *TestLocators.Form.last_name_input, text=last_name)

    def input_email(self, email: str):
        PageNavigation.input_text(self.driver, *TestLocators.Form.email_input, text=email)

    def input_phone_number(self, phone_number: str):
        PageNavigation.input_text(self.driver, *TestLocators.Form.phone_number_input, text=phone_number)

    def input_company_name(self, company_name: str):
        PageNavigation.input_text(self.driver, *TestLocators.Form.company_name_input, text=company_name)

    def input_project_details(self, project_details: str):
        PageNavigation.input_text(self.driver, *TestLocators.Form.project_details_container, text=project_details)

    # def select_how_did_you_hear_about_us(self, hear_about_us_option: str):
    #     PageNavigation.select_option(self.driver, *TestLocators.Form.hear_about_us_select, option=hear_about_us_option)
    #
    # def select_budget(self, budget_option: str):
    #     PageNavigation.select_option(self.driver, *TestLocators.Form.budget_select, option=budget_option)

    def select_how_did_you_hear_about_us(self, hear_about_us_option: str):
        PageNavigation.select_from_dropdown(self.driver, *TestLocators.Form.hear_about_us_dd, option=hear_about_us_option)

    def select_budget(self, budget_option: str):
        PageNavigation.select_from_dropdown(self.driver, *TestLocators.Form.budget_dd, option=budget_option)

    def select_needed_services(self, needed_services: list):
        for service in needed_services:
            PageNavigation.click_on_element(self.driver, *(By.XPATH,
                                                        f"//label[contains(text(), '{service}')]"))

    def fill_mandatory_fields(self, user):
        self.input_first_name(user["firstName"])
        self.input_last_name(user["lastName"])
        self.input_email(user["email"])
        self.select_needed_services(user["neededServices"])

    def fill_all_fields(self, user):
        self.fill_mandatory_fields(user)
        self.input_phone_number(user["phoneNumber"])
        self.select_how_did_you_hear_about_us(user["hearAboutUs"])
        self.select_budget(user["budget"])
        self.select_needed_services(user["neededServices"])
        self.input_project_details(user["projectDetails"])

    def submit_with_invalid_email(self, user_invalid_email):
        self.fill_mandatory_fields(user_invalid_email)

    def check_privacy_policy(self):
        PageNavigation.click_on_element(self.driver, *TestLocators.Form.privacy_policy_checkbox)

    def submit_form(self):
        PageNavigation.click_on_element(self.driver, *TestLocators.Form.send_msg_btn)

    def get_confirmation_message(self):
        return PageNavigation.find_element(self.driver, *TestLocators.Form.comfirmation_msg).text

    def get_invalid_email_message(self):
        return PageNavigation.find_element(self.driver, *TestLocators.Form.email_validation_msg).text