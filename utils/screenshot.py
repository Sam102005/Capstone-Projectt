"""Screenshot helper. Every screenshot is saved to screenshots/<run-id>/ and
queued so the HTML report can embed it."""
import logging
import re
from pathlib import Path

from config import config

log = logging.getLogger(__name__)

_pending = []   # screenshots waiting to be attached to the report
_counter = [0]


def take_screenshot(driver, name: str) -> Path:
    config.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    _counter[0] += 1
    safe = re.sub(r"[^A-Za-z0-9_-]+", "_", name)
    path = config.SCREENSHOT_DIR / f"{_counter[0]:02d}_{safe}.png"
    driver.save_screenshot(str(path))
    _pending.append(path)
    log.info("Screenshot saved: %s", path)
    return path


def pop_pending():
    items = list(_pending)
    _pending.clear()
    return items
