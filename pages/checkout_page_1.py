from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time


class CheckoutPage1(BasePage):
    _first_name = (By.ID, "first-name")
    _last_name = (By.ID, "last-name")
    _zip_code = (By.ID, "postal-code")
    _continue_button = (By.ID, "continue")

    def enter_checkout_info(self, fname, lname, zip_code):
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        
        # Use framework wrappers for automatic logging
        self.type_text(self._first_name, fname)
        self.type_text(self._last_name, lname)
        self.type_text(self._zip_code, zip_code)
        
        # CRITICAL: Small delay for form validation stabilization
        time.sleep(2)
        
        # Use self.click instead of execute_script for visibility
        self.click(self._continue_button) 
        
        # Wait for navigation with explicit 15s timeout
        self.wait_for_url_contains("checkout-step-two.html", timeout=15)

        from pages.checkout_page_2 import CheckoutPage2
        return CheckoutPage2(self.driver)