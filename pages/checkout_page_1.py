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
        
        self.find_element(self._first_name).clear()
        self.type_text(self._first_name, fname)
        
        self.find_element(self._last_name).clear()
        self.type_text(self._last_name, lname)
        
        self.find_element(self._zip_code).clear()
        self.type_text(self._zip_code, zip_code)
        
        # Small delay to ensure form is ready
        time.sleep(0.5)
        
        continue_btn = self.wait.until(EC.presence_of_element_located(self._continue_button))
        self.driver.execute_script("arguments[0].click();", continue_btn)
    
        # Verify the transition happened with longer timeout
        self.wait_for_url_contains("checkout-step-two.html", timeout=15)

        from pages.checkout_page_2 import CheckoutPage2
        return CheckoutPage2(self.driver)