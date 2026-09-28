import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from config import config
from pages.base_page import BasePage

log = logging.getLogger(__name__)


class AccountPage(BasePage):
    # register form
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM = (By.ID, "input-confirm")
    AGREE = (By.CSS_SELECTOR, "input[name='agree']")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
    CREATED_HEADING = (By.XPATH, "//div[@id='content']/h1[contains(., 'Account Has Been Created')]")
    # login form
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    MY_ACCOUNT_HEADING = (By.XPATH, "//div[@id='content']/h2[normalize-space()='My Account']")
    # shared
    DANGER_ALERT = (By.CSS_SELECTOR, ".alert-danger")
    FIELD_ERRORS = (By.CSS_SELECTOR, "div.text-danger")

    # ---- registration (pre-condition so login always has a valid user) ----
    def register(self, data) -> str:
        """Returns 'created' or 'exists'. Raises AssertionError on any other outcome."""
        self.open(config.REGISTER_URL)
        self.type(self.FIRST_NAME, data["firstname"])
        self.type(self.LAST_NAME, data["lastname"])
        self.type(self.EMAIL, data["email"])
        self.type(self.TELEPHONE, data["telephone"])
        self.type(self.PASSWORD, data["password"])
        self.type(self.CONFIRM, data["password"])
        self.click(self.AGREE)
        self.click(self.REGISTER_SUBMIT)

        def outcome(d):
            if d.find_elements(*self.CREATED_HEADING):
                return "created"
            for alert in d.find_elements(*self.DANGER_ALERT):
                if alert.is_displayed():
                    return "error:" + alert.text.strip()
            errors = [e.text.strip() for e in d.find_elements(*self.FIELD_ERRORS)
                      if e.is_displayed() and e.text.strip()]
            if errors:
                return "error:" + "; ".join(errors)
            return False

        try:
            result = WebDriverWait(self.driver, config.EXPLICIT_WAIT).until(outcome)
        except TimeoutException:
            raise AssertionError("Registration did not finish - no success or error message appeared.")

        if result == "created":
            log.info("User %s registered", data["email"])
            return "created"
        if "already registered" in result.lower():
            log.info("User %s already exists - continuing", data["email"])
            return "exists"
        raise AssertionError(f"Registration failed: {result}")

    # ---- login / logout ----
    def login(self, email, password):
        self.open(config.LOGIN_URL)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_SUBMIT)

        def outcome(d):
            if d.find_elements(*self.MY_ACCOUNT_HEADING):
                return "ok"
            for alert in d.find_elements(*self.DANGER_ALERT):
                if alert.is_displayed():
                    return "error:" + alert.text.strip()
            return False

        try:
            result = WebDriverWait(self.driver, config.EXPLICIT_WAIT).until(outcome)
        except TimeoutException:
            raise AssertionError("Login did not finish - 'My Account' page never appeared.")
        if result != "ok":
            raise AssertionError(f"Login failed: {result}")
        log.info("Logged in as %s", email)

    def is_logged_in(self):
        return self.is_visible(self.MY_ACCOUNT_HEADING, timeout=5)

    def logout(self):
        self.open(config.LOGOUT_URL)
        log.info("Logged out")
