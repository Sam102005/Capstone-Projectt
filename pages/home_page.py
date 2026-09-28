import logging

from selenium.webdriver.common.by import By

from config import config
from pages.base_page import BasePage

log = logging.getLogger(__name__)


class HomePage(BasePage):
    SEARCH_BOX = (By.CSS_SELECTOR, "#search input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")

    def open_home(self):
        self.open(config.BASE_URL)

    def is_search_box_visible(self):
        return self.is_visible(self.SEARCH_BOX, timeout=config.EXPLICIT_WAIT)

    def search(self, product_name):
        log.info("Searching for '%s'", product_name)
        self.type(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
