from playwright.sync_api import Page, expect

"""
Page Object representing the logout functionality.

Attributes:
    - open_menu: Locator for the 'Open Menu' button that reveals the sidebar.
    - logout_button: Locator for the 'Logout' link within the menu.

Methods:
    - logout(): Opens the navigation menu and clicks the 'Logout' link to log the user out.
"""


class LogoutPage:
    def __init__(self, page: Page):
        self.page= page
        self.open_menu = page.get_by_role("button", name="Open Menu")
        self.logout_button = page.get_by_role("link", name="Logout")

    def logout(self):
        expect(self.open_menu).to_be_visible()
        expect(self.logout_button).to_be_visible()
        self.open_menu.click()
        self.logout_button.click()
