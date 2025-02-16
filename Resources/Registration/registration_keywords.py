import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "reg_email")
        self.password_input = (By.ID, "reg_password")
        self.register_button = (By.XPATH, "//input[@name='register']")

    def generate_random_email(self):
        return "testuser_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@test.com"

    def generate_random_password(self):
        return "Test@" + ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_input)).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_register(self):
        register_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.register_button)
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.register_button)
        ).click()

    def is_registration_successful(self):
        success_element = (By.XPATH, "//p[contains(text(), 'Thank you for registering') or contains(text(), 'Your account has been created')]")
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(success_element))
