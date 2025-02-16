import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Address.addresses_locators import AddressesLocators
import random

class AddressesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_my_account(self):
        self.wait.until(EC.element_to_be_clickable(AddressesLocators.MY_ACCOUNT)).click()
        logging.info("Clicked on 'My Account'.")

    def navigate_to_addresses(self):
        self.wait.until(EC.element_to_be_clickable(AddressesLocators.ADDRESSES_LINK)).click()
        logging.info("Navigated to the Addresses page.")

    def click_edit_billing_address(self):
        self.driver.find_element(*AddressesLocators.EDIT_BILLING_ADDRESS).click()

    def clear_address_field(self):
        self.driver.find_element(*AddressesLocators.ADDRESS_INPUT).clear()

    def enter_address(self, address):
        self.driver.find_element(*AddressesLocators.ADDRESS_INPUT).send_keys(address)

    def clear_city_field(self):
        self.driver.find_element(*AddressesLocators.CITY_INPUT).clear()

    def enter_city(self, city):
        self.driver.find_element(*AddressesLocators.CITY_INPUT).send_keys(city)

    def clear_pincode_field(self):
        self.driver.find_element(*AddressesLocators.PINCODE_INPUT).clear()

    def enter_pincode(self, pincode):
        self.driver.find_element(*AddressesLocators.PINCODE_INPUT).send_keys(pincode)

    def click_save_address(self):
        self.driver.find_element(*AddressesLocators.SAVE_ADDRESS_BUTTON).click()

    def get_billing_address_text(self):
        wait = WebDriverWait(self.driver, 10)
        billing_address_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='u-column1 col-1 woocommerce-Address']//address"))
        )
        return billing_address_element.text.strip()

    def click_edit_shipping_address(self):
        self.driver.find_element(*AddressesLocators.EDIT_SHIPPING_ADDRESS).click()

    def clear_shipping_address_field(self):
        self.driver.find_element(*AddressesLocators.SHIPPING_ADDRESS_INPUT).clear()

    def clear_shipping_city_field(self):
        self.driver.find_element(*AddressesLocators.SHIPPING_CITY_INPUT).clear()

    def clear_shipping_pincode_field(self):
        self.driver.find_element(*AddressesLocators.SHIPPING_PINCODE_INPUT).clear()

    def enter_shipping_address(self, address):
        self.driver.find_element(*AddressesLocators.SHIPPING_ADDRESS_INPUT).send_keys(address)

    def enter_shipping_city(self, city):
        self.driver.find_element(*AddressesLocators.SHIPPING_CITY_INPUT).send_keys(city)

    def enter_shipping_pincode(self, pincode):
        self.driver.find_element(*AddressesLocators.SHIPPING_PINCODE_INPUT).send_keys(pincode)

    def get_error_message(self):
        error_element = self.wait.until(
            EC.presence_of_element_located(AddressesLocators.ERROR_MESSAGE)
        )
        return error_element.text.strip()