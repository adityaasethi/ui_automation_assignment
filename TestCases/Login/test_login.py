import pytest
import logging
from selenium import webdriver
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Resources.Login.login_keywords import LoginKeywords
from Resources.Login.data_loader import load_test_data
from Resources.test_report_utils import generate_test_summary
from Resources.test_report_utils import print_report_link


logging.basicConfig(
    filename="reports/test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)

test_data = load_test_data("login_data.json")

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practice.automationtesting.in/my-account/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def setup_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practice.automationtesting.in/my-account/")
    yield driver
    driver.quit()


# Positive Case: Pass with valid username/password
@pytest.mark.login
def test_login_valid(setup):
    driver = setup
    login_page = LoginKeywords(driver)

    email = test_data["valid_user"]["email"]
    password = test_data["valid_user"]["password"]

    logging.info(f"Logging in with valid email: {email}")
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login()

    assert login_page.is_login_successful(), "Login failed for valid user!"

# Negative Case: Fail with invalid username/password
@pytest.mark.login
def test_login_invalid(setup):
    driver = setup
    login_page = LoginKeywords(driver)

    email = test_data["invalid_user"]["email"]
    password = test_data["invalid_user"]["password"]

    logging.info(f"Attempting login with invalid email: {email}")
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login()

    assert not login_page.is_login_successful(), "Login should have failed for invalid user!"

# Generate test summary after execution
generate_test_summary()
print_report_link()

