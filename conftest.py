import pytest
import os
from datetime import datetime
from selenium import webdriver

REPORT_DIR = "reports"
if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_path = os.path.join(REPORT_DIR, f"ExtentReport_{timestamp}.html")

@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get("setup")
        if driver:
            screenshot_path = os.path.join(REPORT_DIR, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            pytest_html = item.config.pluginmanager.getplugin("html")
            extra = getattr(item.config, "extra", [])
            extra.append(pytest_html.extras.image(screenshot_path))
            item.config.extra = extra

def pytest_configure(config):
    config.option.htmlpath = report_path
