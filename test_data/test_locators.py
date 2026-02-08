from selenium.webdriver.common.by import By


class TestLocators:

    accept_all_cookies_btn = (By.XPATH, '//button[@aria-label="Accept All"]')

    class Form:
        ## Mandatory fields
        first_name_input = (By.ID, "input_7_5")
        last_name_input = (By.ID, "input_7_18")
        email_input = (By.ID, "input_7_17")
        privacy_policy_checkbox = (By.ID, "input_7_16_1")
        send_msg_btn = (By.ID, "gform_submit_button_7")
        ## Optional fields
        phone_number_input = (By.ID, "input_7_8")
        hear_about_us_select = (By.ID, "input_7_9")
        hear_about_us_dd = (By.ID, "field_7_9")
        company_name_input = (By.ID, "input_7_11")
        budget_select = (By.ID, "input_7_12")
        budget_dd = (By.ID, "field_7_12")
        project_details_container = (By.ID, "input_7_15")
        file_upload = (By.ID, "gform_multifile_upload_7_3")
        ## Validation messages
        first_name_validation_msg = (By.ID, "validation_message_7_5")
        last_name_validation_msg = (By.ID, "validation_message_7_18")
        email_validation_msg = (By.ID, "validation_message_7_17")
        privacy_policy_checkbox_validation_msg = (By.ID, "validation_message_7_16")
        comfirmation_msg = (By.ID, "gform_confirmation_message_7")

        hear_about_option = (By.XPATH, '//li[contains(text(), "Google")]')

