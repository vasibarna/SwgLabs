from playwright.async_api import Page


def test_PageName(page: Page):
    # test that verifies the name of the page
    page.goto("https://www.saucedemo.com/v1/index.html")
    assert "Swag" in page.title()
