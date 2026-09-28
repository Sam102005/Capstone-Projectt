"""Creates the WebDriver. Selenium Manager (built into Selenium 4.6+) downloads
the matching driver automatically, so no manual chromedriver setup is needed."""
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config import config

log = logging.getLogger(__name__)


def create_driver(browser: str = None, headless: bool = None):
    browser = (browser or config.BROWSER).lower()
    headless = config.HEADLESS if headless is None else headless
    log.info("Launching browser=%s headless=%s", browser, headless)

    if browser == "chrome":
        opts = ChromeOptions()
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--disable-notifications")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        opts.add_experimental_option(
            "prefs",
            {"credentials_enable_service": False,
             "profile.password_manager_enabled": False},
        )
        if headless:
            opts.add_argument("--headless=new")
        driver = webdriver.Chrome(options=opts)
    elif browser == "firefox":
        opts = FirefoxOptions()
        if headless:
            opts.add_argument("-headless")
        driver = webdriver.Firefox(options=opts)
    elif browser == "edge":
        opts = EdgeOptions()
        opts.add_argument("--window-size=1920,1080")
        if headless:
            opts.add_argument("--headless=new")
        driver = webdriver.Edge(options=opts)
    else:
        raise ValueError(f"Unsupported browser '{browser}'. Use chrome, firefox or edge.")

    driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
    if not headless:
        try:
            driver.maximize_window()
        except Exception:  # some environments do not support maximize
            pass
    return driver
