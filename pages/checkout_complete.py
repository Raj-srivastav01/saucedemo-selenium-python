from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    _complete_header = (By.CLASS_NAME, "complete-header")

    def get_success_message(self):
        return self.get_text(self._complete_header)