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

#Positive TestCase: After logging in successfully, we navigate to the addresses section, edit the billing address and remove the existing address. We generate random address and save it. After saving we verify if it's reflecting correctly below the name of the account holder in the billing address section.
@pytest.mark.addresses
def test_navigate_to_addresses(setup):
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

    assert login_page.is_login_successful(), "Login failed for valid user!"
    logging.info("Successfully logged in.")

    addresses_page.click_my_account()

    addresses_page.navigate_to_addresses()

    logging.info("Test Passed: Successfully logged in and navigated to Addresses page.")

    logging.info("Clicking the 'Edit' link for Billing Address.")
    addresses_page.click_edit_billing_address()

    random_address = generate_random_string(12)
    random_city = generate_random_string(8)
    random_pincode = generate_random_pincode()

    addresses_page.clear_address_field()
    addresses_page.enter_address(random_address)

    addresses_page.clear_city_field()
    addresses_page.enter_city(random_city)

    addresses_page.clear_pincode_field()
    addresses_page.enter_pincode(random_pincode)

    logging.info(f"Updated Address: {random_address}, City: {random_city}, Pincode: {random_pincode}")

    addresses_page.click_save_address()
    logging.info("Address updated successfully.")

    addresses_page.navigate_to_addresses()
    logging.info("Navigated back to Addresses page.")

    displayed_address = addresses_page.get_billing_address_text()

    assert random_address in displayed_address, (
        f"Address does not match!\nExpected: {random_address}\nGot: {displayed_address}"
    )
