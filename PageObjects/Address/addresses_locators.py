from selenium.webdriver.common.by import By

class AddressesLocators:
    MY_ACCOUNT = (By.XPATH, "//a[text()='My Account']")
    ADDRESSES_LINK = (By.XPATH, "//a[text()='Addresses']")
    EDIT_BILLING_ADDRESS = (By.LINK_TEXT, "Edit")
    ADDRESS_INPUT = (By.ID, "billing_address_1")
    CITY_INPUT = (By.ID, "billing_city")
    STATE_DROPDOWN = (By.ID, "billing_state")
    PINCODE_INPUT = (By.ID, "billing_postcode")

    SAVE_ADDRESS_BUTTON = (By.NAME, "save_address")
    EDIT_SHIPPING_ADDRESS = (By.XPATH, "//div[@class='u-column2 col-2 woocommerce-Address']//a[text()='Edit']")
    SHIPPING_ADDRESS_INPUT = (By.ID, "shipping_address_1")
    SHIPPING_CITY_INPUT = (By.ID, "shipping_city")
    SHIPPING_STATE_DROPDOWN = (By.ID, "shipping_state")
    SHIPPING_PINCODE_INPUT = (By.ID, "shipping_postcode")
    SAVE_SHIPPING_ADDRESS_BUTTON = (By.NAME, "save_address")
    ERROR_MESSAGE = (By.XPATH, "//ul[@class='woocommerce-error']//li")