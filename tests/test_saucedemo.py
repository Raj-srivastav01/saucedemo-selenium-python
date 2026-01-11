from utils.logger_utility import get_logger
from pages.login_page import LoginPage
from config import VALID_USER, VALID_PASSWORD

logger = get_logger("StandardUserE2E")


def test_standard_user_e2e(driver):
    logger.info("=" * 50)
    logger.info("Starting: Standard User E2E Flow")

    login_page = LoginPage(driver)
    inventory = login_page.login(VALID_USER, VALID_PASSWORD)

    inventory.add_item_to_cart("Sauce Labs Backpack")
    cart = inventory.go_to_cart()
    inventory = cart.click_continue_shopping()

    assert "inventory.html" in driver.current_url

    inventory.add_item_to_cart("Sauce Labs Bike Light")
    cart = inventory.go_to_cart()

    cart.remove_item_from_cart("Sauce Labs Backpack")

    checkout_step_1 = cart.start_checkout()
    checkout_step_2 = checkout_step_1.enter_checkout_info("Raj", "Srivastav", "226028")
    receipt_page = checkout_step_2.finish_checkout()

    success_msg = receipt_page.get_success_message()
    assert "Thank you for your order" in success_msg
    logger.info("TEST PASSED: Order completed successfully.")