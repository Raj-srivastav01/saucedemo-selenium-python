from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config import IMPLICIT_WAIT, BASE_URL


class DriverFactory:
    @staticmethod
    def get_driver(browser_type="chrome", options=None):
        if browser_type.lower() == "chrome":
            if options is None:
                options = ChromeOptions()
                options.add_argument("--start-maximized")

            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif browser_type.lower() == "firefox":
            options = FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        else:
            raise ValueError(f"Browser '{browser_type}' is not supported.")

        driver.maximize_window()
        driver.implicitly_wait(IMPLICIT_WAIT)
        driver.get(BASE_URL)

        return driver