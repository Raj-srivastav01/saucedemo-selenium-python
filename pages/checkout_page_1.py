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
        
        # Fill form with explicit waits
        first_name_field = self.find_element(self._first_name)
        first_name_field.clear()
        first_name_field.send_keys(fname)
        time.sleep(0.3)
        
        last_name_field = self.find_element(self._last_name)
        last_name_field.clear()
        last_name_field.send_keys(lname)
        time.sleep(0.3)
        
        zip_field = self.find_element(self._zip_code)
        zip_field.clear()
        zip_field.send_keys(zip_code)
        time.sleep(0.5)
        
        # Wait for form to be fully ready
        time.sleep(1)
        
        # Scroll button into view
        continue_btn = self.wait.until(EC.presence_of_element_located(self._continue_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", continue_btn)
        time.sleep(0.3)
        
        # Try clicking with JS
        self.driver.execute_script("arguments[0].click();", continue_btn)
        
        # Wait for navigation with longer timeout
        self.wait_for_url_contains("checkout-step-two.html", timeout=20)

        from pages.checkout_page_2 import CheckoutPage2
        return CheckoutPage2(self.driver)