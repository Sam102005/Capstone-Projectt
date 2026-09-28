"""Shared fixtures and the report hooks (screenshots are embedded in the HTML report)."""
import base64
import logging

import pytest

from config import config
from utils.data_reader import load_test_data
from utils.driver_factory import create_driver
from utils.screenshot import pop_pending, take_screenshot

try:
    import pytest_html
except ImportError:  # report still works without embedding
    pytest_html = None

log = logging.getLogger(__name__)




@pytest.fixture(scope="session")
def test_data():
    """Test data read from JSON or Excel (DATA_SOURCE)."""
    return load_test_data()


@pytest.fixture(scope="class")
def driver():
    """One browser shared by all steps of a test class."""
    drv = create_driver()
    yield drv
    log.info("Closing browser")
    drv.quit()


@pytest.fixture(autouse=True)
def skip_if_previous_step_failed(request):
    """The steps form one business flow - if one fails, skip the rest."""
    if request.cls is not None and getattr(request.cls, "flow_failed", False):
        pytest.skip("Skipped because an earlier step in the flow failed")


def pytest_html_report_title(report):
    report.title = "Selenium Capstone - E-Commerce Purchase Flow Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    driver = item.funcargs.get("driver")
    if report.failed:
        if item.cls is not None:
            item.cls.flow_failed = True
        if driver is not None:
            try:
                take_screenshot(driver, f"FAILED_{item.name}")
            except Exception as exc:
                log.warning("Could not take failure screenshot: %s", exc)

    if pytest_html is not None:
        extras = getattr(report, "extras", [])
        for path in pop_pending():
            encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
            extras.append(pytest_html.extras.image(encoded, name=path.stem))
        report.extras = extras
