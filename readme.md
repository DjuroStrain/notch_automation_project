# Notch Selenium Project

Notch Selenium Project is test automation project for Notch web application.

It uses Selenium WebDriver for running tests on multiple browsers based on Python programming language and pytest framework.

## Prerequisites
- Python
  - pytest
  - pytest-selenium
  - pytest-allure

## Project Structure
The project is organized as follows:
- `conftest.py`: Driver initialization and screenshot capture configuration.
- `tests/`: Contains test cases and fixtures.
- `tests/base_test.py`: Base test class for all test cases.
- `pages/`: Contains page objects.
- `helpers/`: Contains helper functions and utilities.
- `test_data/`: Contains test data.
- `allure-results/`: Contains Allure report data.

## Test Design
The goal of the automation suite is to validate the functionality of the contact form with a set of test cases.
The test cases are designed to cover the following scenarios:
- Validating the mandatory contact form fields.
- Submitting the contact form with mandatory valid data.
- Submitting the contact form with all data.
- Submitting the contact form with invalid email.
- Submitting the contact form with empty mandatory fields.
These scenarion were chosen because they cover the most critical risks of the contact form.

## Test Implementation
The automation suite follows the Page Object Model pattern where test logic is separated from page interaction logic.
Each page action is created as a small, atomic method in a page object class (eg. insert text into single input field
or click on a button)
Test data as well as element locators are stored in separate files for better maintainability and readability.
Tests are using explicit waits to ensure that the page is loaded before performing any actions. Hard coded waits are not 
used to ensure stability and reliability.
Hard assertion are used to verify the single expected result and soft assertion to verify multiple expected results.
All test results are logged in Allure report with attached screenshots for failed tests.

## Test Execution
To run the tests, execute the following command in the terminal:
```bash
pytest -v --alluredir=allure-results
```
This will run all the tests and generate an Allure report in the `allure-results` directory.
To view the report, run the following command:
```bash
allure serve allure-results
```
This will open the Allure report in a web browser.


