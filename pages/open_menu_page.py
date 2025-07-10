from playwright.sync_api import Page, expect

"""
Page Object representing the navigation menu component.

Attributes:
    - open_menu: Locator for the 'Open Menu' button.

Methods:
    - click_open_menu_button(): Clicks the 'Open Menu' button to expand the sidebar navigation.
"""
class OpenMenu:
    def __init__(self, page: Page):
        self.page= page
        self.open_menu = page.get_by_role("button", name="Open Menu")

    def click_open_menu_button(self):
        expect(self.open_menu).to_be_visible()
        self.open_menu.click()
