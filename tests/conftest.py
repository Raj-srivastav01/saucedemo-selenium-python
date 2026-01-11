import pytest
from utils.driver_factory import DriverFactory
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    _driver = DriverFactory.get_driver("chrome", options=chrome_options)

    yield _driver

    _driver.quit()