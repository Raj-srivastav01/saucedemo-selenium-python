from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger_utility import get_logger
from config import DEFAULT_TIMEOUT
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)
    
    def find_element(self, locator):
        self.logger.info(f"Waiting for element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        self.logger.info(f"Element Clicked: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        self.logger.info(f"Typing '{text}' into {locator}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        text = self.find_element(locator).text
        self.logger.info(f"Retrieved text: '{text}' from {locator}")
        return text
    
    def wait_for_url_contains(self, url_fragment, timeout=None):
        """Explicit wait for URL change"""
        timeout = timeout or DEFAULT_TIMEOUT
        self.logger.info(f"Waiting for URL to contain: {url_fragment}")
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(url_fragment))
            self.logger.info(f"URL now contains: {url_fragment}")
        except TimeoutException:
            current_url = self.driver.current_url
            self.logger.error(f"URL did not change. Current URL: {current_url}")
            raise TimeoutException(f"Expected URL fragment '{url_fragment}' not found. Current URL: {current_url}")