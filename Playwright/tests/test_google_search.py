import re
from playwright.sync_api import expect

def test_google_search(page):
    # Navigate to Google
    page.goto("https://www.google.com")

    # Accept cookies if the prompt appears
    try:
        accept_button = page.locator("button:has-text('I agree')")
        if accept_button.is_visible():
            accept_button.click()
    except Exception as e:
        print(f"No cookie prompt found: {e}")

    # Type the search query into the search box
    search_box = page.get_by_role("combobox", name="Search")
    search_box.fill("Playwright Python")
    page.keyboard.press("Enter")

    # Wait for the results to load and display the results
    #results = page.locator("#search .g")
    #expect(results).to_have_count_greater_than(0)

    # Verify that the first result contains the expected text
    #first_result = results.nth(0)
    expect(page).to_have_title(re.compile(r"Playwright.*Python", re.IGNORECASE))