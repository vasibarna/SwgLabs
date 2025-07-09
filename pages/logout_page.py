from playwright.sync_api import Page

''' 
Attributes: Open Menu, Logout locators
Behaviour: Click on each button/link
'''
class LogoutPage:
    def __init__(self, page: Page):
        self.page= page
        self.open_menu = page.get_by_role("button", name="Open Menu")
        self.logout_button = page.get_by_role("link", name="Logout")

    def logout(self):
        self.open_menu.click()
        self.logout_button.click()