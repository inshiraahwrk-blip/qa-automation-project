# Test data for a login test
site_url = "https://www.saucedemo.com"
valid_user = "standard_user"
invalid_user = "wrong_user"
expected_page = "inventory.html"

# A function that checks if login redirected correctly
def verify_redirect(actual_url, expected_page):
    if expected_page in actual_url:
        print("PASS — redirected correctly to", actual_url)
    else:
        print("FAIL — expected page with:", expected_page, "but got:", actual_url)

# Call 1 — successful login
verify_redirect("https://www.saucedemo.com/inventory.html", expected_page)

# Call 2 — failed login
verify_redirect("https://www.saucedemo.com/", expected_page)

# Call 3 — mini challenge
verify_redirect("https://www.saucedemo.com/cart.html", "cart.html")