import logging
import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
from conftest import URL
from pages.login_page import LoginPage
from config.constants import URL, USERNAME, PASSWORD, URL_LOGGED_IN


@pytest.mark.parametrize("username, password, error", [
    ("", "", "Username is required"),
    (USERNAME, "", "Password is required"),
    (USERNAME, "wrong_password", "Username and password do not match"),
    ("wrong_user", PASSWORD, "Username and password do not match"),
])
def test_invalid_login(page: Page, username, password, error):
    logging.info(f"Invalid login test with user '{username}' and password '{password}'. Expected is: {error} ")
    page.goto(URL)
    login_page = LoginPage(page)
    login_page.login(username, password)
    expect(page.locator("[data-test=\"error\"]")).to_contain_text(error)
    logging.info("Login not successful, as expected")
