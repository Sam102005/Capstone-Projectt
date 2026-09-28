import logging
import re

from selenium.webdriver.common.by import By

from config import config
from pages.base_page import BasePage, xpath_literal

log = logging.getLogger(__name__)


def _money(text: str) -> float:
    match = re.search(r"\d[\d,]*\.?\d*", text)
    if not match:
        raise ValueError(f"No price found in '{text}'")
    return float(match.group().replace(",", ""))


class CartPage(BasePage):
    ROWS = (By.XPATH, "(//div[@id='content']//form)[1]//table//tbody/tr")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    def open_cart(self):
        self.open(config.CART_URL)
        self.find(self.ROWS)   # fails with a clear timeout if the cart is empty

    def get_items(self):
        """Returns one dict per cart row: name, quantity, unit_price, total."""
        items = []
        for row in self.driver.find_elements(*self.ROWS):
            cells = row.find_elements(By.TAG_NAME, "td")
            items.append({
                "name": cells[1].find_element(By.TAG_NAME, "a").text.strip(),
                "quantity": int(row.find_element(
                    By.CSS_SELECTOR, "input[name^='quantity']").get_attribute("value")),
                "unit_price": _money(cells[4].text),
                "total": _money(cells[5].text),
            })
        return items

    def update_quantity(self, product_name, quantity) -> str:
        lit = xpath_literal(product_name)
        row = f"//tr[.//a[normalize-space()={lit}]]"
        qty_box = (By.XPATH, row + "//input[starts-with(@name,'quantity')]")
        update_btn = (By.XPATH, row + "//button[.//i[contains(@class,'fa-refresh')]]")
        self.type(qty_box, quantity)
        self.click(update_btn)
        message = self.find_visible(self.SUCCESS_ALERT).text.strip()
        log.info("Cart update message: %s", message)
        return message
