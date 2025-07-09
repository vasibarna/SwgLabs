import logging
from config.constants import URL, URL_LOGGED_IN
from playwright.sync_api import expect
from pages.logout_page import LogoutPage


def test_successful_logout(login, page):
    logging.info(f"Logout from page: '{URL_LOGGED_IN}'")
    logout_page = LogoutPage(page)
    logout_page.logout()
    expect(page).to_have_url(URL)
    logging.info("Test passed successfully")
