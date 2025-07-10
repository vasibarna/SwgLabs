from playwright.sync_api import Page, expect

"""
Page Object utility for interacting with product-specific links.

Attributes:
    - link: Locator for a link element matching the given product name.

Methods:
    - click_on(): Clicks the matched product link.
"""


class GetLink:
    def __init__(self, page: Page, product_name):
        self.page = page
        self.link = page.get_by_role("link", name=product_name, exact=False)

    def click_on(self):
        expect(self.link).to_be_visible()
        self.link.click()
