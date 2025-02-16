# UI Automation Framework

This is a Selenium-based UI automation framework using Python and Pytest. It follows the Page Object Model (POM) structure for maintainability and scalability.

## Project Structure

```
ui_automation_assignment/
│-- PageObjects/       # Contains POM classes with locators
│-- Resources/         # Contains business logic (keywords)
│-- TestCases/         # Contains test cases
│-- TestData/          # Contains test data in JSON format
│-- reports/           # Stores generated HTML reports
│-- requirements.txt   # Lists required dependencies
│-- README.md          # Project documentation
```

## Dependencies

Install the required dependencies using:
```bash
pip install -r requirements.txt
```

Additional dependencies used in this framework:
```bash
pip install pytest 
pip install pytest-html 
pip install pytest-metadata
```

## How to Run the Tests

To execute the tests, use the following commands:

### Run all test cases with Extent Report:
Navigate to project root: cd ui_automation_assignment
```bash
 pytest --html=reports/ExtentReport.html --self-contained-html
```
### Run a specific test file:
```bash
pytest TestCases/Login/test_login.py --html=reports/login_report.html
```

### Run tests by marker:
```bash
pytest -m addresses --html=reports/address_test_report.html
```

## Test Case Overview

### Login Tests
Positive:
- **test_login_valid_user**: Verifies successful login with valid credentials.
Negative:
- **test_login_invalid_user**: Checks login failure with incorrect credentials and causes a failure.

### Address Tests
Positive:
- **test_billing_address**: Validates updating the billing address and asserting the saved details. 
Negative:
- **test_shipping_address_negative**: Tries to save an empty shipping address to verify error handling and causes a failure.

### Cart Tests
Positive:
- **test_add_to_cart**: Adds items to the cart and verifies they appear correctly.
- **test_remove_from_cart**: Removes items from the cart and ensures they are deleted successfully.
Negative:
- **test_remove_wrong_product**: Adds two products, and removes the wrong/unexpected one and causes a failure.

### Registration Tests
Positive:
- **test_register_new_user**: Attempts user registration with unique credentials.
Negative:
- **test_register_existing_user**: Tries registering an already registered email to confirm proper error handling and causes a failure.

### Extent Reports Integration
This framework integrates **Extent Reports** using `pytest-html`. Screenshots are automatically captured and attached in case of failures.

---
This documentation provides a comprehensive guide to understanding and running the framework. 🚀

