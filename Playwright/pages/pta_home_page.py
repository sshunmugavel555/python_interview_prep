from playwright.sync_api import Page, expect

class HomePage:
    """ A Page Object Model (POM) class for the home page of the application."""

    def __init__(self, page:Page):
        self.page = page
        self.pta_link = page.get_by_role("link", name="Practice Test Automation", exact=True)
        self.logged_in_heading = page.get_by_role("heading")
        self.logout_article = page.get_by_role("article")
        self.logout_link = page.get_by_role("link", name="Log out")

    def is_link_visible(self):
        expect(self.pta_link).to_be_visible()

    def is_logged_in(self):
        expect(self.logged_in_heading).to_contain_text("Logged In Successfully")

    def is_logout_visible(self):
        expect(self.logout_article).to_contain_text("Log out")

    def click_logout(self):
        self.logout_link.click()