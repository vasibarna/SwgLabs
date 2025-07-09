import logging
import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
from conftest import URL


@pytest.mark.parametrize("username, password, error", [
    ("", "", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("standard_user", "standard_user", "Username and password do not match"),
    ("wrong_user", "secret_sauce", "Username and password do not match"),
])
def test_invalid_login(page: Page, username, password, error):
    page.goto(URL)
    logging.info(f"Invalid login test with user '{username}' and password '{password}'. Expected is: {error} ")
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.get_by_role("button", name="LOGIN").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text(error)
