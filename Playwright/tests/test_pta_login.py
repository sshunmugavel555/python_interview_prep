import re
from playwright.sync_api import Page, expect
from pages.pta_login_page import LoginPage
from pages.pta_home_page import HomePage

def test_login(page: Page) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    # Verify that the username input is visible
    expect(login_page.username_input).to_be_visible()
    
    # Fill in the username and password fields
    login_page.enter_username("student")
    login_page.enter_password("Password123")
    
    # Verify that the input values are correct
    expect(login_page.username_input).to_have_value("student")
    expect(login_page.password_input).to_have_value("Password123")
    
    # Click the submit button
    login_page.click_submit()
    
    # Verify successful login
    home_page.is_link_visible()
    home_page.is_logged_in()
    home_page.is_logout_visible()