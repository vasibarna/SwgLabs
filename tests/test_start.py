import time

import pytest
from playwright.async_api import Page

@pytest.mark.smoke
def test_page_name(page: Page):
    # test that verifies the name of the page
    page.goto("https://www.saucedemo.com/v1/index.html")
    assert "Swag" in page.title()


@pytest.mark.integration
def test_products_list(login_logout, page: Page):
    page.get_by_text("Products")
    page.get_by_role("button", name="Open Menu")

