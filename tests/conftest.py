import pytest
from appium import webdriver
import allure
import os
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app = r"C:\appium\bucketplace-inc.apk"
    options.app_package = "com.bucketplace.homes"
    options.app_activity = "com.bucketplace.homes.MainActivity"
    options.automation_name = "UiAutomator2"
    options.no_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = os.path.join("allure-results", f"{item.name}.png")
            os.makedirs("allure-results", exist_ok=True)
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name=item.name, attachment_type=allure.attachment_type.PNG)
