import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import pytest
import logging
import random
import string
from TestCases.Login.test_login import setup
from Resources.Login.login_keywords import LoginKeywords
from Resources.Address.addresses_keywords import AddressesPage
from TestData.data_loader import load_test_data


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_pincode():
    return str(random.randint(100000, 999999))

#Negative TestCase: After logging in successfully, we navigate to the addresses section, edit the shipping address and remove the existing address. We enter empty details and save it. After saving we verify if it's throwing an error of mandatory fields not filled. If not, we fail the testcase.
@pytest.mark.addresses
def test_invalid_shipping_address(setup):
    driver = setup
    login_page = LoginKeywords(driver)
    addresses_page = AddressesPage(driver)

    test_data = load_test_data("login_data.json")
    email = test_data["valid_user"]["email"]
    password = test_data["valid_user"]["password"]

    logging.info(f"Logging in with valid email: {email}")
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login()
    assert login_page.is_login_successful(), "Login failed!"
    logging.info("Successfully logged in.")

    addresses_page.click_my_account()
    addresses_page.navigate_to_addresses()
    logging.info("Navigated to Addresses page.")

    logging.info("Clicking 'Edit' for Shipping Address.")
    addresses_page.click_edit_shipping_address()

    addresses_page.clear_shipping_address_field()
    addresses_page.enter_shipping_address("")

    addresses_page.clear_shipping_city_field()
    addresses_page.enter_shipping_city("")

    addresses_page.clear_shipping_pincode_field()
    addresses_page.enter_shipping_pincode("")

    logging.info("Entered empty values for shipping details.")

    addresses_page.click_save_address()

    error_message = addresses_page.get_error_message()

    expected_error = "This field is optional."

    assert error_message == expected_error, (
        f"Test Failed Intentionally! Expected: '{expected_error}', but got: '{error_message}'"
    )

    logging.info("Test should have failed, but it passed unexpectedly!")