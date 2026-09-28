"""Central configuration. Every value can be overridden with an environment variable."""
import os
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ---- Application under test -------------------------------------------------
BASE_URL = os.getenv("BASE_URL", "https://tutorialsninja.com/demo/").rstrip("/") + "/"
REGISTER_URL = BASE_URL + "index.php?route=account/register"
LOGIN_URL = BASE_URL + "index.php?route=account/login"
LOGOUT_URL = BASE_URL + "index.php?route=account/logout"
CART_URL = BASE_URL + "index.php?route=checkout/cart"

# ---- Browser ----------------------------------------------------------------
BROWSER = os.getenv("BROWSER", "chrome").lower()          # chrome | firefox | edge
HEADLESS = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))     # seconds
PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "60"))

# ---- Test data --------------------------------------------------------------
DATA_SOURCE = os.getenv("DATA_SOURCE", "json").lower()    # json | excel
JSON_DATA_FILE = BASE_DIR / "test_data" / "testdata.json"
EXCEL_DATA_FILE = BASE_DIR / "test_data" / "testdata.xlsx"

# ---- Output folders ---------------------------------------------------------
RUN_ID = datetime.now().strftime("%Y%m%d_%H%M%S")
SCREENSHOT_DIR = BASE_DIR / "screenshots" / RUN_ID
REPORT_DIR = BASE_DIR / "reports"
LOG_DIR = BASE_DIR / "logs"
