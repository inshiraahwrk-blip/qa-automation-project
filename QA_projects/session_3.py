# All test cases — including one broken one to simulate a crash
test_cases = [
    {"url": "https://www.saucedemo.com/inventory.html", "expected": "inventory.html"},
    {"url": "https://www.saucedemo.com/",               "expected": "inventory.html"},
    {"url": "https://www.saucedemo.com/cart.html",      "expected": "cart.html"},
    {"url": None,                                        "expected": "checkout.html"},
    {"url": "https://www.saucedemo.com/",               "expected": "cart.html"},
]

passed = 0
failed = 0
errors = 0

def verify_redirect(actual_url, expected_page):
    global passed, failed, errors
    try:
        if expected_page in actual_url:
            print("PASS — redirected correctly to", actual_url)
            passed += 1
        else:
            print("FAIL — expected:", expected_page, "but got:", actual_url)
            failed += 1
    except Exception as e:
        print("ERROR — something went wrong:", e)
        errors += 1

# Run all test cases
for test in test_cases:
    verify_redirect(test["url"], test["expected"])

# Summary
print("-----------------------------")
print("Total:", passed + failed + errors, "| Passed:", passed, "| Failed:", failed, "| Errors:", errors)