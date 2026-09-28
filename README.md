
# E-Commerce Website Automation Using Selenium and Pytest

## Capstone Project 1

An end-to-end web automation testing framework developed using Python, Selenium WebDriver, Pytest and the Page Object Model (POM) design pattern.

The project automates an e-commerce shopping workflow on the TutorialsNinja OpenCart demo website, including user registration, login, product search, adding a product to the cart, updating product quantity, validating cart details and logging out.

It supports multiple browsers, JSON and Excel test data, automatic screenshots, execution logging and HTML test reports.

---

## 1. Application Under Test

**Website:** https://tutorialsninja.com/demo/

**Application:** TutorialsNinja OpenCart Demo Store

**Testing Type:** End-to-End Functional Automation Testing

**Automation Framework:** Selenium WebDriver with Pytest

**Programming Language:** Python

**Design Pattern:** Page Object Model (POM)

---

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.9+ | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution and assertions |
| pytest-html | HTML test reporting |
| openpyxl | Excel test data management |
| JSON | Data-driven testing |
| Page Object Model | Framework architecture |
| Selenium Manager | Automatic browser driver management |
| VS Code | Development environment |
| Git | Version control |

---

## 3. Features

The framework provides the following functionality:

- Automated browser initialization and termination.
- Automatic registration of a customer account.
- Login using valid customer credentials.
- Product searching and validation.
- Adding products to the shopping cart.
- Updating product quantities.
- Verification of product names, quantities and prices.
- Validation of the calculated cart total.
- Customer logout.
- Screenshot capture at important execution steps.
- JSON and Excel-based test data.
- HTML test report generation.
- Execution logging.
- Cross-browser support.
- Headless browser execution.
- Configurable explicit waits and page-load timeouts.

---

## 4. Project Structure

```text
Capstone_1/
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── account_page.py
│   ├── search_page.py
│   └── cart_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_purchase_flow.py
│
├── test_data/
│   ├── testdata.json
│   ├── testdata.xlsx
│   └── create_excel.py
│
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py
│   ├── data_reader.py
│   └── screenshot.py
│
├── screenshots/
│
├── reports/
│
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── venv/
```

### Directory Description

**config/**

Contains application configuration, browser settings, timeouts, test data paths and environment variable handling.

**pages/**

Contains Page Object Model classes. Each class encapsulates the elements and operations associated with a particular application page.

**tests/**

Contains the eight automated test cases that execute the complete e-commerce workflow.

**test_data/**

Stores the JSON and Excel files used for data-driven testing.

**utils/**

Contains reusable utilities for browser initialization, reading test data and capturing screenshots.

**screenshots/**

Stores screenshots captured during test execution. Each execution has its own timestamped directory.

**reports/**

Contains the generated HTML test report.

**logs/**

Stores detailed execution logs.

**conftest.py**

Defines shared Pytest fixtures, browser setup, test data initialization and reporting hooks.

**pytest.ini**

Contains the default Pytest execution and reporting configuration.

**requirements.txt**

Lists the Python dependencies required to execute the project.

---

# 5. Prerequisites

Before running the project, ensure the following software is installed.

### 5.1 Python

Python 3.9 or newer is required.

Download Python from:

https://www.python.org/downloads/

During installation, enable:

`Add Python to PATH`

Verify the installation:

```powershell
python --version
```

If Python is installed correctly, the terminal will display its version.

### 5.2 Visual Studio Code

Download and install Visual Studio Code:

https://code.visualstudio.com/

Install the Microsoft Python extension in VS Code.

### 5.3 Google Chrome

Install Google Chrome:

https://www.google.com/chrome/

Chrome is the default browser used by the automation framework.

Firefox and Microsoft Edge are also supported.

### 5.4 Internet Connection

An active internet connection is required to access the demo website.

Selenium Manager may also need internet access to download the appropriate browser driver during the first execution.

---

# 6. Installation and Environment Setup

The following instructions are intended for Windows users running the project through the VS Code PowerShell terminal.

## Step 1: Extract the Project

Extract the downloaded `Capstone_1.zip` file.

For example, extract it to:

```text
C:\Users\sayan\OneDrive\Desktop\Capstone_1
```

Make sure the extracted directory contains:

```text
requirements.txt
pytest.ini
conftest.py
tests/
pages/
config/
```

If the ZIP creates an additional nested `Capstone_1` directory, open the inner directory containing these files.

## Step 2: Open the Project in VS Code

Open Visual Studio Code.

Select:

```text
File → Open Folder
```

Select the extracted project folder.

Open the integrated terminal:

```text
Terminal → New Terminal
```

Navigate to the project directory:

```powershell
cd C:\Users\sayan\OneDrive\Desktop\Capstone_1
```

Verify that you are in the correct directory:

```powershell
dir
```

You should see `requirements.txt`, `pytest.ini` and the other project files.

## Step 3: Create a Virtual Environment

A Python virtual environment isolates the project's dependencies from other Python installations.

If you extracted the ZIP file and it already contains a `venv` folder, delete that folder before creating a fresh environment.

You can delete it using File Explorer or the following PowerShell command:

```powershell
Remove-Item -Recurse -Force .\venv
```

Run this deletion command only if the existing `venv` directory is present.

Create a fresh virtual environment:

```powershell
python -m venv venv
```

Wait for the command to finish.

A new `venv` directory will be created inside the project.

## Step 4: Resolve the PowerShell Execution Policy Error

Windows PowerShell may prevent virtual environment activation and display the following error:

```text
Activate.ps1 cannot be loaded because
running scripts is disabled on this system.
```

To resolve this issue, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

This temporarily permits script execution in the current PowerShell session.

The original execution policy is restored when the terminal session ends.

If your organization's security policy prevents this change, use Command Prompt and run `venv\Scripts\activate.bat` instead.

## Step 5: Activate the Virtual Environment

Execute:

```powershell
.\venv\Scripts\Activate.ps1
```

After successful activation, the terminal should display:

```text
(venv) PS C:\Users\sayan\OneDrive\Desktop\Capstone_1>
```

The `(venv)` prefix indicates that the virtual environment is active.

## Step 6: Upgrade pip

Execute:

```powershell
python -m pip install --upgrade pip
```

## Step 7: Install Project Dependencies

Install all required packages:

```powershell
python -m pip install -r requirements.txt
```

The project uses the following dependencies:

```text
selenium>=4.15,<5
pytest>=7.4,<9
pytest-html==4.1.1
openpyxl>=3.1
```

Wait until installation finishes successfully.

## Step 8: Verify Installation

Check the installed Pytest version:

```powershell
python -m pytest --version
```

Check the installed Selenium package:

```powershell
python -m pip show selenium
```

Both commands should display the installed package information without errors.

---

# 7. Running the Complete Automation Project

## Step 1: Activate the Virtual Environment

Whenever you open a new PowerShell terminal, navigate to the project folder and activate the environment.

```powershell
cd C:\Users\sayan\OneDrive\Desktop\Capstone_1
```

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

```powershell
.\venv\Scripts\Activate.ps1
```

## Step 2: Verify Test Discovery

Before executing the automation, check whether Pytest can discover the test cases.

```powershell
python -m pytest --collect-only -q
```

Expected result:

```text
8 tests collected
```

## Step 3: Execute All Tests

Run:

```powershell
python -m pytest
```

This command executes the complete automation workflow using the configuration defined in `pytest.ini`.

The browser should launch automatically.

The framework will execute the eight test cases in their defined order.

Do not manually interact with the automated browser during execution.

## Step 4: Review the Results

After execution, Pytest displays the result of each test case.

A successful execution should show all eight tests as passed.

The actual result depends on the availability and behavior of the demo website and the successful execution of each automation step.

If a test fails, the framework intentionally skips the remaining dependent tests.

---

# 8. Automated Test Cases

The project implements eight test cases.

| Test ID | Test Case | Expected Result |
|---|---|---|
| TC01 | Launch browser and open application | Homepage loads successfully |
| TC02 | Register customer account | Account is created or an existing account is recognized |
| TC03 | Login | Customer logs in successfully |
| TC04 | Search product | Expected product appears in search results |
| TC05 | Add product to cart | Product is added successfully |
| TC06 | Update product quantity | Cart quantity is updated |
| TC07 | Verify cart details | Product, quantity, unit price and total are correct |
| TC08 | Logout | Customer logs out successfully |

### Test Execution Flow

```text
START
  |
  v
Launch Browser
  |
  v
Open E-Commerce Website
  |
  v
Register Customer Account
  |
  v
Login
  |
  v
Search Product
  |
  v
Add Product to Cart
  |
  v
Update Quantity
  |
  v
Verify Cart Details
  |
  v
Logout
  |
  v
Generate Test Report
  |
  v
END
```

All eight tests share the same browser session.

The framework uses automatic customer registration to ensure that valid login credentials are available.

A unique email address can be generated for each execution using a timestamp.

---

# 9. Test Data Management

The framework supports two test data sources:

- JSON
- Excel

JSON is the default data source.

The relevant files are:

```text
test_data/testdata.json
test_data/testdata.xlsx
```

The test data contains customer registration details, login credentials, the product name and the quantity to be used during execution.

## 9.1 JSON Test Data

To use JSON test data, execute:

```powershell
$env:DATA_SOURCE = "json"
python -m pytest
```

The framework reads the data from:

```text
test_data/testdata.json
```

## 9.2 Excel Test Data

To use Excel test data, execute:

```powershell
$env:DATA_SOURCE = "excel"
python -m pytest
```

The framework reads the data from:

```text
test_data/testdata.xlsx
```

The Excel workbook contains a worksheet named `TestData`.

## 9.3 Regenerate the Excel File

After updating the source data, regenerate the Excel workbook using:

```powershell
python test_data/create_excel.py
```

Note that this script creates the workbook from its defined data. Review the script before running it if you have made manual changes to the existing Excel file.

## 9.4 Modify the Product and Quantity

The test data can be customized by changing the following fields:

```text
product_name
update_quantity
```

For example, the project can search for a different available product and update the cart quantity accordingly.

The product must exist on the demo website.

---

# 10. Browser Configuration

The framework supports three browsers:

1. Google Chrome
2. Mozilla Firefox
3. Microsoft Edge

Google Chrome is used by default.

Browser selection is controlled through the `BROWSER` environment variable.

## Run Using Chrome

```powershell
$env:BROWSER = "chrome"
python -m pytest
```

## Run Using Firefox

```powershell
$env:BROWSER = "firefox"
python -m pytest
```

Firefox must be installed before executing this command.

## Run Using Microsoft Edge

```powershell
$env:BROWSER = "edge"
python -m pytest
```

Microsoft Edge must be installed before executing this command.

Selenium Manager automatically handles compatible browser drivers when possible.

---

# 11. Headless Browser Execution

Headless execution allows the tests to run without displaying the browser window.

This mode is useful for automated testing environments and CI/CD pipelines.

Enable headless execution:

```powershell
$env:HEADLESS = "true"
python -m pytest
```

Disable headless execution:

```powershell
$env:HEADLESS = "false"
python -m pytest
```

The default configuration uses a visible browser window.

---

# 12. Configuration and Environment Variables

The central configuration file is:

```text
config/config.py
```

The following environment variables are supported:

| Variable | Default | Description |
|---|---|---|
| BASE_URL | https://tutorialsninja.com/demo/ | Application URL |
| BROWSER | chrome | Browser selection |
| HEADLESS | false | Headless execution |
| EXPLICIT_WAIT | 20 | Explicit wait in seconds |
| PAGE_LOAD_TIMEOUT | 60 | Page-load timeout in seconds |
| DATA_SOURCE | json | Test data source |

### Example: Increase Explicit Wait

If the demo website is loading slowly, increase the explicit wait:

```powershell
$env:EXPLICIT_WAIT = "40"
python -m pytest
```

### Example: Increase Page-Load Timeout

```powershell
$env:PAGE_LOAD_TIMEOUT = "90"
python -m pytest
```

### Example: Run Firefox with Excel Data

```powershell
$env:BROWSER = "firefox"
$env:DATA_SOURCE = "excel"

python -m pytest
```

Environment variables set in PowerShell remain active for the current terminal session.

To return to the default configuration, close the terminal and open a new one.

---

# 13. HTML Test Reports

The project uses `pytest-html` to generate an HTML execution report.

Report generation is already configured in `pytest.ini`.

The default report location is:

```text
reports/report.html
```

After test execution, open the report using:

```powershell
Start-Process .\reports\report.html
```

The report provides information about the test execution, including passed, failed and skipped test cases.

The framework also embeds captured screenshots in the report.

The report is self-contained, making it convenient to share the execution results.

Running the tests again may overwrite the previous report. Save a copy if you need to preserve an earlier execution.

---

# 14. Screenshot Capture

The framework automatically captures screenshots at important stages of the test execution.

These include:

- Homepage loading
- Customer registration
- Successful login
- Product search
- Adding a product to the cart
- Cart before quantity update
- Cart after quantity update
- Cart verification
- Customer logout

Screenshots are stored inside:

```text
screenshots/
```

Each execution creates a timestamped screenshot directory.

For example:

```text
screenshots/
    YYYYMMDD_HHMMSS/
        home_page.png
        logged_in.png
        search_results.png
```

Screenshots help with test debugging, execution verification and reporting.

---

# 15. Execution Logs

The project automatically generates execution logs.

The log file is located at:

```text
logs/execution.log
```

Logging is configured through `pytest.ini`.

The logs provide information about test execution, browser initialization, application interactions and errors.

To view the log file in PowerShell:

```powershell
Get-Content .\logs\execution.log
```

To open it in VS Code:

```powershell
code .\logs\execution.log
```

---

# 16. Framework Architecture

The framework follows the Page Object Model design pattern.

Each application page has a dedicated Python class containing its page-specific elements and interactions.

This separates test logic from browser interaction logic.

### Base Page

`pages/base_page.py`

Contains reusable Selenium methods and common page interactions.

### Home Page

`pages/home_page.py`

Handles homepage navigation and product searching.

### Account Page

`pages/account_page.py`

Handles customer registration, login and logout.

### Search Page

`pages/search_page.py`

Handles product search results and adding products to the cart.

### Cart Page

`pages/cart_page.py`

Handles cart navigation, quantity updates and cart validation.

### Test Layer

`tests/test_purchase_flow.py`

Contains the automated test cases and their assertions.

### Utility Layer

The `utils` directory contains browser initialization, test data reading and screenshot utilities.

This architecture improves code reuse, readability and maintainability.

---

# 17. Troubleshooting

## Problem 1: PowerShell Script Execution Is Disabled

Error:

```text
Activate.ps1 cannot be loaded because
running scripts is disabled on this system.
```

Solution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Alternatively, open Command Prompt and execute:

```cmd
venv\Scripts\activate.bat
```

## Problem 2: Virtual Environment Is Not Activating

Verify that the `venv` directory exists.

If the environment is damaged or was created on another computer, delete it and recreate it:

```powershell
python -m venv venv
```

Activate it again:

```powershell
.\venv\Scripts\Activate.ps1
```

## Problem 3: Pytest Is Not Installed

Error:

```text
No module named pytest
```

Solution:

Activate the virtual environment and reinstall the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Verify the installation:

```powershell
python -m pytest --version
```

## Problem 4: ChromeDriver Error

The framework uses Selenium Manager for automatic driver management.

If browser initialization fails:

1. Ensure Google Chrome is installed.
2. Update Google Chrome.
3. Verify that your internet connection is working.
4. Check whether your firewall or network blocks driver downloads.
5. Update Selenium within the versions supported by the project.

If automatic driver management is blocked, install the compatible browser driver manually and make it available on your system PATH.

## Problem 5: Website Is Loading Slowly

Increase the explicit wait:

```powershell
$env:EXPLICIT_WAIT = "40"
```

Increase the page-load timeout if necessary:

```powershell
$env:PAGE_LOAD_TIMEOUT = "90"
```

Run the tests again:

```powershell
python -m pytest
```

## Problem 6: A Test Fails and Remaining Tests Are Skipped

The eight test cases represent a single end-to-end workflow and share the same browser session.

If an earlier test fails, the remaining dependent tests are intentionally skipped.

Check:

```text
reports/report.html
```

Also inspect:

```text
screenshots/
logs/execution.log
```

Identify and resolve the original failure before rerunning the test suite.

## Problem 7: Report Is Not Generated

Verify that all dependencies are installed:

```powershell
python -m pip install -r requirements.txt
```

Confirm that `pytest.ini` exists in the project root.

Run the test suite again:

```powershell
python -m pytest
```

Check the `reports` directory for `report.html`.

---

# 18. Complete Execution Commands

For a fresh installation on Windows, follow the commands below.

Open the project folder in VS Code and start a PowerShell terminal.

If the ZIP contains an existing virtual environment, delete the old `venv` folder before beginning.

### One-Time Setup

```powershell
# Navigate to the project directory

cd C:\Users\sayan\OneDrive\Desktop\Capstone_1

# Create a virtual environment

python -m venv venv

# Temporarily allow PowerShell script execution

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Activate the virtual environment

.\venv\Scripts\Activate.ps1

# Upgrade pip

python -m pip install --upgrade pip

# Install all required dependencies

python -m pip install -r requirements.txt

# Verify Pytest installation

python -m pytest --version

# Check test discovery

python -m pytest --collect-only -q
```

### Execute the Project

```powershell
# Run the complete automation suite

python -m pytest
```

### View the Report

```powershell
# Open the generated HTML report

Start-Process .\reports\report.html
```

### Subsequent Executions

After completing the initial setup, use the following commands whenever you want to run the project again:

```powershell
cd C:\Users\sayan\OneDrive\Desktop\Capstone_1

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\venv\Scripts\Activate.ps1

python -m pytest

Start-Process .\reports\report.html
```

---

# 19. Expected Outcome

After successful execution, the framework should:

- Launch the configured browser.
- Open the TutorialsNinja e-commerce website.
- Register or recognize a customer account.
- Log in with valid credentials.
- Search for the configured product.
- Add the product to the shopping cart.
- Update the product quantity.
- Validate the cart details and calculated total.
- Log out of the customer account.
- Capture execution screenshots.
- Generate execution logs.
- Produce an HTML test report.

All eight tests should pass when the application is available and behaves as expected.

The project automates the shopping-cart workflow; it does not submit an actual checkout or payment.

---

# 20. Conclusion

This capstone project demonstrates the implementation of an end-to-end web automation testing framework using Python, Selenium WebDriver and Pytest.

It incorporates the Page Object Model design pattern, reusable utilities, data-driven testing, cross-browser execution, screenshot capture, execution logging and automated HTML reporting.

The framework provides a structured and maintainable approach to testing a typical e-commerce user journey.
