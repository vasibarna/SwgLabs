import logging
from playwright.sync_api import expect
from config.constants import URL, USERNAME, PASSWORD, URL_LOGGED_IN
from pages.login_page import LoginPage


def test_successful_login(page):
    logging.info("Navigating to login page")
    page.goto(URL)
    login_page = LoginPage(page)
    login_page.login(USERNAME, PASSWORD)
    expect(page).to_have_url(URL_LOGGED_IN)
    logging.info("Test passed successfully")