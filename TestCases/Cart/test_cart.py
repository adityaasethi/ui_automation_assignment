import pytest
import logging
from selenium import webdriver
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Resources.Cart.cart_keywords import CartPage
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
    driver.get("https://practice.automationtesting.in/shop/")
    yield driver
    driver.quit()

# Positive Case: Validating adding the product and reflecting the same product in the cart
@pytest.mark.cart
def test_add_and_validate_product(setup):
    driver = setup
    cart_page = CartPage(driver)

    product_text = cart_page.scroll_to_product()
    logging.info(f"Product selected: {product_text}")

    cart_page.add_product_to_cart()
    cart_page.go_to_cart()

    cart_product_text = cart_page.get_cart_product_name()
    logging.info(f"Product in Cart: {cart_product_text}")

    assert product_text == cart_product_text, "The product in the cart does not match the selected product!"
    logging.info("Test Passed: Product successfully added and validated in the cart.")

# Positive Case: Validating adding the product and removing the same product in the cart
@pytest.mark.cart
def test_add_and_remove_product(setup):
    driver = setup
    cart_page = CartPage(driver)

    cart_page.scroll_to_product()
    cart_page.add_product_to_cart()
    cart_page.go_to_cart()
    logging.info("Product added successfully to the cart.")

    cart_page.remove_product_from_cart()
    logging.info("Product removed successfully from the cart.")

#Negative Case: Adding two products and removing the wrong one from the cart which fails the testcase
@pytest.mark.cart
def test_remove_wrong_product(setup):
    driver = setup
    cart_page = CartPage(driver)

    cart_page.add_both_products_to_cart()
    cart_page.go_to_cart()
    logging.info("Two products added successfully to the cart.")

    cart_page.remove_specific_product_from_cart("HTML5 Forms")
    remaining_products = cart_page.get_cart_product_name()

    if "Mastering JavaScript" in remaining_products:
        logging.error("Test Failed as expected: The wrong product was NOT removed!")
        assert False, "Intentional Failure: The wrong product was removed!"
    else:
        logging.info("Unexpectedly Passed: Correct product was removed.")


# Generate test summary after execution
generate_test_summary()
print_report_link()

