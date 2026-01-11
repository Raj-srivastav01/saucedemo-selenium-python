from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time


class InventoryPage(BasePage):
    _cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    _product_sort = (By.CLASS_NAME, "product_sort_container")
    _inventory_item = (By.CLASS_NAME, "inventory_item")

    def add_item_to_cart(self, product_name):
        dynamic_locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.logger.info(f"Adding {product_name} to cart.")
        self.click(dynamic_locator)

    def remove_item_from_cart(self, product_name):
        dynamic_locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[text()='Remove']")
        self.click(dynamic_locator)

    def go_to_cart(self):
        self.logger.info("Navigating to Cart page")
        
        # Small delay to ensure page is ready
        time.sleep(0.3)
        
        cart_icon = self.wait.until(EC.presence_of_element_located(self._cart_icon))
        self.driver.execute_script("arguments[0].click();", cart_icon)
        
        # Wait for navigation to complete
        self.wait_for_url_contains("cart.html")
        
        from pages.cart_page import CartPage
        return CartPage(self.driver)
    
    def get_all_item_images(self):
        images = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_img img")
        return [img.get_attribute("src") for img in images]