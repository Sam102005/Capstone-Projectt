import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage, xpath_literal

log = logging.getLogger(__name__)


class SearchPage(BasePage):
    RESULT_TITLES = (By.CSS_SELECTOR, ".product-thumb h4 a")
    RESULT_CARDS = (By.CSS_SELECTOR, ".product-thumb")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    def result_titles(self):
        self.wait.until(EC.presence_of_element_located(self.RESULT_CARDS))
        return [e.text.strip() for e in self.driver.find_elements(*self.RESULT_TITLES)]

    def add_to_cart(self, product_name) -> str:
        """Clicks 'Add to Cart' on the card with the given title; returns the success message."""
        lit = xpath_literal(product_name)
        button = (By.XPATH,
                  f"//div[contains(@class,'product-thumb')][.//h4/a[normalize-space()={lit}]]"
                  f"//button[contains(@onclick,'cart.add')]")
        self.click(button)
        message = self.find_visible(self.SUCCESS_ALERT).text.strip()
        log.info("Add to cart message: %s", message)
        return message
