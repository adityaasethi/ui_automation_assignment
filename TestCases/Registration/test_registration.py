import pytest
import logging
from selenium import webdriver
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Resources.Registration.registration_keywords import RegistrationPage
from Resources.test_report_utils import generate_test_summary, print_report_link

logging.basicConfig(
    filename="reports/test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practice.automationtesting.in/my-account/")
    yield driver
    driver.quit()

# Positive Case: Pass with random generation of email/password everytime a new registration is done
@pytest.mark.registration
def test_register_new_user(setup):
    driver = setup
    registration_page = RegistrationPage(driver)

    email = registration_page.generate_random_email()
    password = registration_page.generate_random_password()

    logging.info(f"Attempting registration with email: {email}")

    try:
        registration_page.enter_email(email)
        registration_page.enter_password(password)
        registration_page.click_register()

        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='woocommerce-MyAccount-content']"))
            )
            logging.info("Registration successful!")
            assert True
        except:
            logging.error("Registration failed! Success locator not found.")
            assert False, "Registration failed!"

    except Exception as e:
        logging.error(f"Test failed due to: {str(e)}")
        raise

# Negative Case: Fail with same email/password registration
@pytest.mark.registration
def test_register_existing_user(setup):
    driver = setup
    registration_page = RegistrationPage(driver)

    email = "adisethi7@gmail.com"
    password = "zxcvbnmA@199807"

    logging.info(f"Attempting registration with an existing email: {email}")

    try:
        registration_page.enter_email(email)
        registration_page.enter_password(password)
        registration_page.click_register()

        error_locator = "//li[contains(text(), 'An account is already registered with your email address. Please login.')]"
        if driver.find_elements(By.XPATH, error_locator):
            logging.error("Test failed! An account is already registered with this email.")
            assert False, "An account is already registered with your email address. Please login."

        logging.info("No duplicate account error found. Registration might have succeeded unexpectedly.")

    except Exception as e:
        logging.error(f"Test failed due to: {str(e)}")
        raise

# Generate test summary after execution
generate_test_summary()
print_report_link()
