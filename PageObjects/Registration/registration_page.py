from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "reg_email")  # Change locator as per actual ID
        self.password_input = (By.ID, "reg_password")  # Change locator as per actual ID
        self.register_button = (By.XPATH, "//input[@name='register']")


