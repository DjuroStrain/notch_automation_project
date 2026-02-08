import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import allure


@pytest.fixture(scope="session", params=["chrome", "firefox", "safari"])
def browser(request):
    return request.param


@pytest.fixture(autouse=True)
def driver(request, browser):
    driver = None
    match browser:
        case 'chrome':
            driver = webdriver.Chrome()
        case 'firefox':
            driver = webdriver.Firefox()
        case 'safari':
            driver = webdriver.Safari()
        case _:
            raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    driver.get('https://wearenotch.com/qa_task/')
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    driver = item.funcargs.get("driver", None)
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Screenshot",
                attachment_type=AttachmentType.PNG
            )
