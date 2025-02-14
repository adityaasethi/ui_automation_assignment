import logging
from selenium.webdriver.common.by import By

class LoginKeywords:
    """Reusable login functions"""

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        """Enter email in the login form"""
        logging.info(f"Entering email: {email}")
        self.driver.find_element(By.ID, "username").send_keys(email)

    def enter_password(self, password):
        """Enter password in the login form"""
        logging.info("Entering password")
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        """Click the login button"""
        logging.info("Clicking the login button")
        self.driver.find_element(By.NAME, "login").click()

    def is_login_successful(self):
        """Check if login is successful"""
        return "my-account" in self.driver.current_url
