from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage2(BasePage):
    _finish_btn = (By.ID, "finish")
    _total_label = (By.CLASS_NAME, "summary_total_label")

    def get_total_price(self):
        return self.get_text(self._total_label)

    def finish_checkout(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        
        finish_btn = self.wait.until(EC.presence_of_element_located(self._finish_btn))
        self.driver.execute_script("arguments[0].click();", finish_btn)

        from pages.checkout_complete import CheckoutCompletePage
        return CheckoutCompletePage(self.driver)