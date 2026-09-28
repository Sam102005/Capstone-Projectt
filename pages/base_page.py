"""Base page: explicit waits, safe click/type, and JavaScript alert handling."""
import logging

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import config

log = logging.getLogger(__name__)


def xpath_literal(text: str) -> str:
    """Safely quote a string for use inside an XPath expression."""
    if "'" not in text:
        return f"'{text}'"
    if '"' not in text:
        return f'"{text}"'
    parts = text.split("'")
    return "concat(" + ", \"'\", ".join(f"'{p}'" for p in parts) + ")"


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

    # ---- navigation ----
    def open(self, url):
        log.info("Opening %s", url)
        self.driver.get(url)
        self.handle_alert()

    # ---- element helpers ----
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def _scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self._scroll_into_view(element)
        try:
            element.click()
        except (ElementClickInterceptedException,
                ElementNotInteractableException,
                StaleElementReferenceException):
            log.warning("Normal click failed for %s - using JavaScript click", locator)
            element = self.find(locator)
            self.driver.execute_script("arguments[0].click();", element)
        self.handle_alert()

    def type(self, locator, text, clear=True):
        element = self.find_visible(locator)
        if clear:
            element.clear()
        element.send_keys(str(text))

    def text_of(self, locator):
        return self.find_visible(locator).text.strip()

    # ---- popup / alert handling ----
    def handle_alert(self, accept=True, timeout=0.5):
        """Accept (or dismiss) a JavaScript alert/confirm if one is present.
        Returns the alert text, or None when there was no alert."""
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        except TimeoutException:
            return None
        text = alert.text
        log.info("JavaScript alert found: '%s' -> %s", text, "accept" if accept else "dismiss")
        alert.accept() if accept else alert.dismiss()
        return text
