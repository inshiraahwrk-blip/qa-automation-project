# Import Selenium's browser controller
from selenium import webdriver

# Import the "By" class — tells Selenium HOW to find elements (by ID, name, etc.)
from selenium.webdriver.common.by import By

# Import WebDriverWait — smarter waiting than time.sleep
from selenium.webdriver.support.ui import WebDriverWait

# Import expected_conditions — defines WHAT to wait for (URL change, element appears, etc.)
from selenium.webdriver.support import expected_conditions as EC

# Import time — for simple fixed waits when needed
import time

# ---- COUNTERS ----
# These track how many tests passed and failed across ALL test cases
passed = 0
failed = 0

# ---- FUNCTION ----
# This function runs ONE login test
# username, password → what to type into the form
# expected → "pass" means we expect login to succeed, "fail" means we expect it to be rejected
def test_login(username, password, expected):
    
    # Tell Python to use the global passed/failed variables, not create new local ones
    global passed, failed
    
    # Open a fresh Chrome browser window
    driver = webdriver.Chrome()
    
    # Make the browser full screen so elements are visible
    driver.maximize_window()
    
    # Navigate to the SauceDemo login page
    driver.get("https://www.saucedemo.com")
    
    # Create a wait object — will wait UP TO 10 seconds for things to appear
    wait = WebDriverWait(driver, 10)
    
    # Don't do anything until the username field actually exists on the page
    wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    
    # Find the username input field by its ID and type the username into it
    driver.find_element(By.ID, "user-name").send_keys(username)
    
    # Find the password input field by its ID and type the password into it
    driver.find_element(By.ID, "password").send_keys(password)
    
    # Find the login button by its ID and click it
    driver.find_element(By.ID, "login-button").click()
    
    # ---- ASSERTION FOR VALID LOGIN ----
    # If we expected this login to succeed...
    if expected == "pass":
        
        # Wait until the URL contains "inventory" — means login worked and page changed
        wait.until(EC.url_contains("inventory"))
        
        # Read the current URL after login
        current_url = driver.current_url
        
        # Check if "inventory" is in the URL — confirms we landed on the right page
        if "inventory" in current_url:
            print("PASS — Login successful!")
            passed += 1   # increment pass counter
        else:
            print("FAIL — Expected success but got:", current_url)
            failed += 1   # increment fail counter
    
    # ---- ASSERTION FOR INVALID LOGIN ----
    # If we expected this login to be rejected...
    elif expected == "fail":
        
        # Wait 2 seconds — invalid login won't change the URL so we can't use url_contains
        time.sleep(2)
        
        # Read the current URL — should still be the login page
        current_url = driver.current_url
        
        # If "inventory" is NOT in the URL — login was correctly rejected
        if "inventory" not in current_url:
            print("PASS — Correctly rejected invalid login!")
            passed += 1   # increment pass counter
        else:
            print("FAIL — Invalid login somehow succeeded!")
            failed += 1   # increment fail counter
    
    # Close the browser after each test — next test opens a fresh one
    driver.quit()


# ---- TEST DATA ----
# A list of dictionaries — each one is a test case with its own credentials and expected result
test_cases = [
    {"username": "standard_user", "password": "secret_sauce",  "expected": "pass"},
    {"username": "wrong_user",    "password": "wrong_password", "expected": "fail"},
]

# ---- RUN ALL TESTS ----
# Loop through every test case in the list
# enumerate gives us both the index (i) and the test data
for i, test in enumerate(test_cases):
    
    # Print which test is running — i+1 because index starts at 0
    print(f"\n--- Test {i+1} ---")
    
    # Call the function with this test case's data
    test_login(test["username"], test["password"], test["expected"])

# ---- SUMMARY ----
# After all tests are done, print the final score
print("\n-----------------------------")
print(f"Total: {passed+failed} | Passed: {passed} | Failed: {failed}")