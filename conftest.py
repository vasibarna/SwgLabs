import pytest
from playwright.sync_api import Page, expect
import logging
from config.constants import URL, USERNAME, PASSWORD, URL_LOGGED_IN
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


@pytest.fixture(scope="function")
def login(page: Page):
    # login on the pate
    logging.info(f"Navigating to page: '{URL}' and login")
    page.goto(URL)
    login_page = LoginPage(page)
    login_page.login(USERNAME, PASSWORD)
    # execute the test
    yield page


@pytest.fixture(scope="function")
def authenticated_page(page: Page):
    # login on the pate
    logging.info(f"Navigating to page: '{URL}' and login")
    page.goto(URL)
    login_page = LoginPage(page)
    login_page.login(USERNAME, PASSWORD)

    # execute the test
    yield page

    # logout from the page
    logging.info(f"Logout from page: '{URL_LOGGED_IN}'")
    logout_page = LogoutPage(page)
    logout_page.logout()
    expect(page).to_have_url(URL)
