import re
import pytest
from playwright.async_api import Page
from playwright.sync_api import expect

LOGIN_URL = "https://www.saucedemo.com/v1/index.html"


@pytest.mark.smoke
def test_page_name(page: Page):
    # test that verifies the name of the page
    page.goto(LOGIN_URL)
    assert "Swag" in page.title()


@pytest.mark.integration
def test_logged_in_dashboard_elements_visible(login_logout, page: Page):
    assert page.get_by_text("Products").is_visible()
    assert page.get_by_role("button", name="Open Menu").is_visible()


@pytest.mark.parametrize("username, password, error", [
    ("", "", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("standard_user", "standard_user", "Username and password do not match"),
    ("wrong_user", "secret_sauce", "Username and password do not match"),
])
def test_invalid_login(page: Page, username, password, error):
    page.goto(LOGIN_URL)
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.get_by_role("button", name="LOGIN").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text(error)



