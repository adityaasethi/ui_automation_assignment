from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "username")  # Change locator as per actual ID
        self.password_input = (By.ID, "password")  # Change locator as per actual ID
        self.login_button = (By.XPATH, "//button[@type='submit']")

    # def enter_email(self, email):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
    #
    # def enter_password(self, password):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
    #
    # def click_login(self):
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
