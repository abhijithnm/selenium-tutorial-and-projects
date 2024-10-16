# Selenium 4 with Python: Complete Tutorial (Basic to Advanced)

This guide will help you get started with Selenium 4 for browser automation using Python, covering everything from basic to advanced topics.

## Table of Contents

1. [Introduction to Selenium 4](#introduction-to-selenium-4)
2. [Installation and Setup](#installation-and-setup)
3. [Basic Selenium WebDriver Commands](#basic-selenium-webdriver-commands)
4. [Locating Elements](#locating-elements)
5. [Interacting with Web Elements](#interacting-with-web-elements)
6. [Waiting Mechanisms (Implicit and Explicit Waits)](#waiting-mechanisms-implicit-and-explicit-waits)
7. [Handling Browser Navigation and Windows](#handling-browser-navigation-and-windows)
8. [Working with Forms and IFrames](#working-with-forms-and-iframes)
9. [Handling Alerts, Popups, and Dialogs](#handling-alerts-popups-and-dialogs)
10. [Taking Screenshots](#taking-screenshots)
11. [Advanced Topics](#advanced-topics)
    - Working with Shadow DOM
    - Handling JavaScript and AJAX
    - Headless Browsing
    - Handling Cookies and Sessions
    - Mobile Emulation
    - Running Tests in Parallel
12. [Best Practices for Writing Selenium Tests](#best-practices-for-writing-selenium-tests)
13. [Integrating with Unit Testing Frameworks](#integrating-with-unit-testing-frameworks)
14. [Debugging and Logging in Selenium](#debugging-and-logging-in-selenium)

---

## 1. Introduction to Selenium 4

Selenium is an open-source tool for automating web browsers. It’s commonly used for testing web applications. Selenium 4 introduces new features like:

- Enhanced WebDriver API
- Support for Chrome DevTools Protocol (CDP)
- Full support for W3C WebDriver standards

---

## 2. Installation and Setup

### Step 1: Install Selenium

```bash
pip install selenium
```

### Step 2: Install WebDriver

Download a browser driver like [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads) or [GeckoDriver (Firefox)](https://github.com/mozilla/geckodriver/releases) and add it to your system PATH.

### Step 3: Verify Installation

```python
from selenium import webdriver

driver = webdriver.Chrome()  # or webdriver.Firefox()
driver.get("https://www.google.com")
driver.quit()
```

---

## 3. Basic Selenium WebDriver Commands

- **Opening a Website**:

```python
driver.get('https://www.example.com')
```

- **Getting the Title of the Page**:

```python
print(driver.title)
```

- **Closing the Browser**:

```python
driver.quit()  # Closes all windows
```

---

## 4. Locating Elements

- **By ID**:

```python
element = driver.find_element_by_id('element_id')
```

- **By XPath**:

```python
element = driver.find_element_by_xpath('//tag[@attribute="value"]')
```

- **By CSS Selector**:

```python
element = driver.find_element_by_css_selector('css_selector')
```

---

## 5. Interacting with Web Elements

- **Clicking an Element**:

```python
element.click()
```

- **Typing in a Text Box**:

```python
element.send_keys('Your text here')
```

- **Getting Text of an Element**:

```python
print(element.text)
```

---

## 6. Waiting Mechanisms (Implicit and Explicit Waits)

- **Implicit Wait**:

```python
driver.implicitly_wait(10)
```

- **Explicit Wait**:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "myElement"))
)
```

---

## 7. Handling Browser Navigation and Windows

- **Back and Forward Navigation**:

```python
driver.back()  # Go back
driver.forward()  # Go forward
```

- **Switching Between Windows**:

```python
windows = driver.window_handles
driver.switch_to.window(windows[1])  # Switch to the second window
```

---

## 8. Working with Forms and IFrames

- **Working with Forms**:

```python
input_field = driver.find_element_by_id("input_id")
input_field.send_keys("Test text")
input_field.submit()
```

- **Switching to an IFrame**:

```python
driver.switch_to.frame("iframe_name_or_id")
driver.switch_to.default_content()  # Switch back to the main content
```

---

## 9. Handling Alerts, Popups, and Dialogs

- **Handling Alerts**:

```python
alert = driver.switch_to.alert
alert.accept()  # Accept the alert
```

---

## 10. Taking Screenshots

```python
driver.save_screenshot('screenshot.png')
```

---

## 11. Advanced Topics

### 1. **Working with Shadow DOM**:

```python
shadow_host = driver.find_element_by_css_selector("shadow_host")
shadow_root = shadow_host.shadow_root
element_inside_shadow = shadow_root.find_element_by_css_selector("element_selector")
```

### 2. **Handling JavaScript and AJAX**:

```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

### 3. **Headless Browsing**:

```python
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
```

### 4. **Handling Cookies and Sessions**:

```python
driver.get_cookies()
driver.add_cookie({"name": "my_cookie", "value": "cookie_value"})
```

### 5. **Mobile Emulation**:

```python
mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=chrome_options)
```

### 6. **Running Tests in Parallel**:

Install `pytest-xdist` for parallel testing:

```bash
pip install pytest-xdist
```

Run tests using:

```bash
pytest -n 4  # Run tests in 4 parallel threads
```

---

## 12. Best Practices for Writing Selenium Tests

1. Use **Page Object Model (POM)** to organize your code.
2. Use **explicit waits** to prevent flaky tests.
3. Externalize test data (e.g., JSON or configuration files).
4. Ensure proper resource cleanup (e.g., using `try-finally` to close browsers).

---

## 13. Integrating with Unit Testing Frameworks

### **Using unittest**:

```python
import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_example(self):
        self.driver.get("http://example.com")
        self.assertIn("Example", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

### **Using pytest**:

```python
def test_example():
    driver = webdriver.Chrome()
    driver.get("http://example.com")
    assert "Example" in driver.title
    driver.quit()
```

---

## 14. Debugging and Logging in Selenium

### **Logging**:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

---

## Conclusion

This `README.md` covers a comprehensive guide from basic to advanced Selenium 4 usage in Python.
