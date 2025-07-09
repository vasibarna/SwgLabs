from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page= page
        self.username_field = page.locator("[id='user-name']")
        self.password_field = page.locator("[id='password']")
        self.login_button = page.locator("text=LOGIN")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()