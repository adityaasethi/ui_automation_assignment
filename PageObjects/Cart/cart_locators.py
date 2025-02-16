from selenium.webdriver.common.by import By

class CartLocators:

    # Product locators
    HTML5_PRODUCT = (By.XPATH, "//h3[text()='HTML5 Forms']")
    Mastering_JavaScript = (By.XPATH, "//h3[text()='Mastering JavaScript']")
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//a[@data-product_id='181']")
    ADD_TO_BASKET_MS_BUTTON = (By.XPATH, "//a[@data-product_id='165']")
    # Cart locators
    VIEW_CART_BUTTON = (By.XPATH, "//a[contains(@title, 'View your shopping cart')]")
    CART_PRODUCT_NAME = (By.XPATH, "//td[@class='product-name']/a")
    REMOVE_PRODUCT_BUTTON = (By.XPATH, "//a[@class='remove']")
