import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.locator("#form")).to_contain_text("Username")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("Password123")
    expect(page.get_by_role("textbox", name="Username")).to_have_value("student");
    expect(page.get_by_role("textbox", name="Password")).to_have_value("Password123");
    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_role("link", name="Practice Test Automation", exact=True)).to_be_visible()
    expect(page.get_by_role("heading")).to_contain_text("Logged In Successfully")
    expect(page.get_by_role("article")).to_contain_text("Log out")
    
    page.get_by_role("link", name="Log out").click()
