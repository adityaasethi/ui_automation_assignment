import logging

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PageObjects.Cart.cart_locators import CartLocators
import logging

class CartPage:
    """Methods to interact with the Cart page"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def scroll_to_product(self):
        for _ in range(5):
            try:
                html5_product = self.wait.until(EC.visibility_of_element_located(CartLocators.HTML5_PRODUCT))
                add_to_cart = self.wait.until(EC.element_to_be_clickable(CartLocators.ADD_TO_BASKET_BUTTON))
                self.actions.move_to_element(html5_product).perform()
                return html5_product.text
            except:
                self.driver.execute_script("window.scrollBy(0, 300);")  # Scroll down in steps
                continue

    def add_product_to_cart(self):
        html5_product = self.wait.until(EC.visibility_of_element_located(CartLocators.HTML5_PRODUCT))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", html5_product)
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        if iframes:
            self.driver.switch_to.frame(iframes[0])
            self.driver.execute_script("window.scrollBy(0, 300);")
            self.driver.switch_to.default_content()
        add_to_cart = self.wait.until(EC.element_to_be_clickable(CartLocators.ADD_TO_BASKET_BUTTON))

        try:
            add_to_cart.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", add_to_cart)

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(CartLocators.VIEW_CART_BUTTON)).click()

    def get_cart_product_name(self):
        return self.wait.until(EC.presence_of_element_located(CartLocators.CART_PRODUCT_NAME)).text

    def remove_product_from_cart(self):
        remove_button = self.wait.until(EC.element_to_be_clickable(CartLocators.REMOVE_PRODUCT_BUTTON))
        remove_button.click()

        self.wait.until(EC.invisibility_of_element_located(CartLocators.CART_PRODUCT_NAME))
        logging.info("Product has been successfully removed from the shopping cart!")

    def add_both_products_to_cart(self):
        try:
            logging.info("Attempting to add 'HTML5 Forms' to cart...")
            html5_product = self.wait.until(EC.presence_of_element_located(CartLocators.HTML5_PRODUCT))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", html5_product)

            add_html5 = self.wait.until(EC.element_to_be_clickable(CartLocators.ADD_TO_BASKET_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_html5)

            try:
                add_html5.click()
                logging.info("Clicked 'Add to Cart' for HTML5 Forms")
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", add_html5)
                logging.info("Click intercepted! Used JavaScript click for HTML5 Forms")

            self.wait.until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-message"), "added to your cart"))
            logging.info("'HTML5 Forms' successfully added to the cart")

        except Exception as e:
            logging.error(f"Failed to add 'HTML5 Forms' to cart: {e}")
        try:
            logging.info("Attempting to add 'Mastering JavaScript' to cart...")
            js_product = self.wait.until(EC.presence_of_element_located(CartLocators.Mastering_JavaScript))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", js_product)

            add_js = self.wait.until(EC.element_to_be_clickable(CartLocators.ADD_TO_BASKET_MS_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_js)

            try:
                add_js.click()
                logging.info("Clicked 'Add to Cart' for Mastering JavaScript")
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", add_js)
                logging.info("Click intercepted! Used JavaScript click for Mastering JavaScript")

            self.wait.until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-message"), "added to your cart"))
            logging.info("'Mastering JavaScript' successfully added to the cart")

        except Exception as e:
            logging.error(f"Failed to add 'Mastering JavaScript' to cart: {e}")

        logging.info("Both products ('HTML5 Forms' & 'Mastering JavaScript') have been added to the cart.")

    def remove_specific_product_from_cart(self, product_name):

        product_elements = self.driver.find_elements(*CartLocators.CART_PRODUCT_NAME)

        for product in product_elements:
            if product.text == product_name:
                remove_button = product.find_element(By.XPATH, "../../..//a[@class='remove']")
                remove_button.click()
                self.wait.until(EC.invisibility_of_element_located(
                    (By.XPATH, f"//td[@class='product-name']/a[text()='{product_name}']")))
                logging.info(f"Product '{product_name}' has been removed from the cart.")
                return

        logging.error(f"Product '{product_name}' not found in cart!")


