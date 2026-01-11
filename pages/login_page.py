from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    _username_field = (By.ID, "user-name")
    _password_field = (By.ID, "password")
    _login_btn = (By.ID, "login-button")
    _error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        self.logger.info(f"Attempting login for user: {username}")
        self.type_text(self._username_field, username)
        self.type_text(self._password_field, password)
        self.click(self._login_btn)
        return InventoryPage(self.driver)
    
    def get_error_message(self):
        return self.get_text(self._error_message)