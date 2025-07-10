from playwright.sync_api import Page, expect

"""
Page Object representing the login screen.

Attributes:
    - username_field: Locator for the username input field.
    - password_field: Locator for the password input field.
    - login_button: Locator for the login button labeled 'LOGIN'.

Methods:
    - login(username, password): Fills in the username and password fields and clicks the login button to 
    attempt authentication.
"""


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("[id='user-name']")
        self.password_field = page.locator("[id='password']")
        self.login_button = page.locator("text=LOGIN")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        expect(self.login_button).to_be_visible()
        self.login_button.click()
