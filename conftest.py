import pytest
from playwright.async_api import Page
from secrets import USERNAME, PASSWORD


@pytest.fixture(scope="function")
def login_logout(page: Page):
    page.goto("https://www.saucedemo.com/v1/index.html")
    page.locator("[id='user-name']").fill(USERNAME)
    page.locator("[id='password']").fill(PASSWORD)
    page.click("text=LOGIN")
    yield
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()
