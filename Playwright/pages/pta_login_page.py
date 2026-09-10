from playwright.sync_api import Page

class LoginPage:
    """ A Page Object Model (POM) class for the login page of the application."""

    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="Submit")

    def enter_username(self, username : str):
        self.username_input.fill(username)

    def enter_password(self, password : str):
        self.password_input.fill(password)

    def click_submit(self):
        self.submit_button.click()