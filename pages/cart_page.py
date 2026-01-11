from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time


class CartPage(BasePage):
    _checkout_button = (By.ID, "checkout")
    _continue_shopping = (By.ID, "continue-shopping")

    def remove_item_from_cart(self, product_name):
        locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']//button")
        
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_list")))
        
        element = self.wait.until(EC.presence_of_element_located(locator))
        
        self.logger.info(f"Removing {product_name} from cart.")
        self.driver.execute_script("arguments[0].click();", element)

    def click_continue_shopping(self):
        self.logger.info("Clicking Continue Shopping")
        element = self.wait.until(EC.presence_of_element_located(self._continue_shopping))
        self.driver.execute_script("arguments[0].click();", element)
        
        # Wait for navigation
        self.wait_for_url_contains("inventory.html")
        
        # CRITICAL: Add delay to let inventory page fully reload
        time.sleep(0.5)
        
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    def start_checkout(self):
        self.logger.info("Starting checkout")
        element = self.wait.until(EC.presence_of_element_located(self._checkout_button))
        self.driver.execute_script("arguments[0].click();", element)
        
        from pages.checkout_page_1 import CheckoutPage1
        return CheckoutPage1(self.driver)