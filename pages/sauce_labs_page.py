from playwright.sync_api import Page, expect

"""
Represents the Sauce Lab landing page.

Attributes:
    - Locates 'Sign in' and 'Search' buttons using ARIA roles.

Methods:
    - verify_sign_in_button(): Checks that the 'Sign in' button is visible.
    - verify_search_button(): Checks that the 'Search' button is visible.
"""
class SauceLab:
    def __init__(self, page: Page):
        self.page= page
        self.sign_in = page.get_by_role("button", name="Sign in")
        self.search = page.get_by_role("button", name="search")

    def verify_sign_in_button(self):
        expect(self.sign_in).to_be_visible()

    def verify_search_button(self):
        expect(self.search).to_be_visible()