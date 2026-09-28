"""End-to-end business scenario: customer buys a product from the demo store.

The steps run in order and share one browser. If a step fails, the remaining
steps are skipped (see conftest.py)."""
import logging

import pytest

from pages.account_page import AccountPage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utils.screenshot import take_screenshot

log = logging.getLogger(__name__)


class TestPurchaseFlow:

    def test_01_launch_browser_and_open_application(self, driver):
        home = HomePage(driver)
        home.open_home()
        take_screenshot(driver, "home_page")
        assert home.is_search_box_visible(), "Home page did not load (search box not found)"

    def test_02_register_user_precondition(self, driver, test_data):
        account = AccountPage(driver)
        result = account.register(test_data)
        take_screenshot(driver, f"registration_{result}")
        assert result in ("created", "exists")
        account.logout()

    def test_03_login(self, driver, test_data):
        account = AccountPage(driver)
        account.login(test_data["email"], test_data["password"])
        take_screenshot(driver, "logged_in")
        assert account.is_logged_in(), "'My Account' page not displayed after login"

    def test_04_search_product(self, driver, test_data):
        home = HomePage(driver)
        home.open_home()
        home.search(test_data["product_name"])
        titles = SearchPage(driver).result_titles()
        take_screenshot(driver, "search_results")
        assert test_data["product_name"] in titles, \
            f"'{test_data['product_name']}' not in search results {titles}"

    def test_05_add_product_to_cart(self, driver, test_data):
        message = SearchPage(driver).add_to_cart(test_data["product_name"])
        take_screenshot(driver, "added_to_cart")
        assert "success" in message.lower(), f"Unexpected message: {message}"
        assert test_data["product_name"].lower() in message.lower()

    def test_06_update_quantity(self, driver, test_data):
        cart = CartPage(driver)
        cart.open_cart()
        take_screenshot(driver, "cart_before_update")
        message = cart.update_quantity(test_data["product_name"], test_data["update_quantity"])
        take_screenshot(driver, "cart_after_update")
        assert "success" in message.lower(), f"Unexpected message: {message}"

    def test_07_verify_cart_details(self, driver, test_data):
        cart = CartPage(driver)
        cart.open_cart()
        items = cart.get_items()
        log.info("Cart contents: %s", items)
        take_screenshot(driver, "cart_verification")

        matches = [i for i in items if i["name"] == test_data["product_name"]]
        assert matches, f"'{test_data['product_name']}' not found in cart: {items}"
        item = matches[0]
        assert item["quantity"] == test_data["update_quantity"], \
            f"Expected quantity {test_data['update_quantity']}, found {item['quantity']}"
        expected_total = round(item["unit_price"] * item["quantity"], 2)
        assert item["total"] == pytest.approx(expected_total, abs=0.01), \
            f"Total {item['total']} != unit price {item['unit_price']} x qty {item['quantity']}"

    def test_08_logout(self, driver):
        AccountPage(driver).logout()
        take_screenshot(driver, "logged_out")
        assert any(k in driver.current_url.lower() for k in ("logout", "login")), driver.current_url
