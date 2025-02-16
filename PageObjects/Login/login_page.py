from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "username")  # Change locator as per actual ID
        self.password_input = (By.ID, "password")  # Change locator as per actual ID
        self.login_button = (By.XPATH, "//button[@type='submit']")
