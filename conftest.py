import pytest
from playwright.async_api import Page

LOGIN_URL = "https://www.saucedemo.com/v1/index.html"

@pytest.fixture(scope="function")
def login_logout(page: Page):
    print(f"\nLOGIN ON WEB PAGE: '{LOGIN_URL}'")
    page.goto(LOGIN_URL)
    page.locator("[id='user-name']").fill("standard_user")
    page.locator("[id='password']").fill("secret_sauce")
    page.click("text=LOGIN")
    yield
    print(f"\nLOGOUT FROM WEB PAGE: '{LOGIN_URL}'")
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()
