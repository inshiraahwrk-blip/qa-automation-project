**# Manual Testing — SauceDemo Login Page

## Test Cases

### TC001 — Valid login with correct username and password
- **Preconditions:** Browser open, on https://www.saucedemo.com, valid credentials exist
- **Steps:**
  1. Enter "standard_user" in username field
  2. Enter "secret_sauce" in password field
  3. Click Login button
- **Expected:** Redirected to https://www.saucedemo.com/inventory.html
- **Status:** PASS

---

### TC002 — Invalid login with wrong credentials
- **Preconditions:** Browser open, on https://www.saucedemo.com
- **Steps:**
  1. Enter "wrong_user" in username field
  2. Enter "wrong_password" in password field
  3. Click Login button
- **Expected:** "Epic sadface: Username and password do not match any user in this service" shown
- **Status:** PASS

---

### TC003 — Login with empty username
- **Preconditions:** Browser open, on https://www.saucedemo.com, valid password available
- **Steps:**
  1. Leave username field blank
  2. Enter "secret_sauce" in password field
  3. Click Login button
- **Expected:** "Epic sadface: Username is required" shown
- **Status:** PASS

---

### TC004 — Login with empty password
- **Preconditions:** Browser open, on https://www.saucedemo.com, valid username available
- **Steps:**
  1. Enter "standard_user" in username field
  2. Leave password field blank
  3. Click Login button
- **Expected:** "Epic sadface: Password is required" shown
- **Status:** PASS

---

### TC005 — Login with both fields empty
- **Preconditions:** Browser open, on https://www.saucedemo.com
- **Steps:**
  1. Leave username field blank
  2. Leave password field blank
  3. Click Login button
- **Expected:** "Epic sadface: Username is required" shown
- **Status:** PASS

---

## Bug Reports

### BUG001 — Page heading shows "Swag Labs" instead of "Sauce Labs"
- **Environment:** Chrome, Windows 11
- **Severity:** Low
- **Priority:** Low
- **Steps:**
  1. Open https://www.saucedemo.com
  2. Login with standard_user / secret_sauce
  3. Observe the page heading
- **Expected:** Heading shows "Sauce Labs"
- **Actual:** Heading shows "Swag Labs"

---

### BUG002 — Product name displays code syntax instead of proper name
- **Environment:** Chrome, Windows 11
- **Severity:** Low
- **Priority:** Low
- **Steps:**
  1. Open https://www.saucedemo.com
  2. Login with standard_user / secret_sauce
  3. Observe product names on inventory page
- **Expected:** All products display proper names
- **Actual:** One product shows "Test.allTheThings() T-Shirt (Red)" — contains code syntax**
