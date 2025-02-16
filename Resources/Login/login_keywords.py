import logging
from selenium.webdriver.common.by import By

class LoginKeywords:

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        logging.info(f"Entering email: {email}")
        self.driver.find_element(By.ID, "username").send_keys(email)

    def enter_password(self, password):
        logging.info("Entering password")
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        logging.info("Clicking the login button")
        self.driver.find_element(By.NAME, "login").click()

    def is_login_successful(self):
        return "my-account" in self.driver.current_url
