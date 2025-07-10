from playwright.sync_api import Page, expect

"""
Page Object for the product detail view.

Attributes:
    - back_button: Locator for the 'Back' navigation button.
    - product_name: Locator for the displayed product name.

Methods:
    - click_back_button(): Navigates back to the inventory list.
    - verify_product_name(expected_text): Verifies that the product name contains the expected text.
"""


class ProductPage:
    def __init__(self, page: Page):
        self.page= page
        self.back_button = page.get_by_role("button", name="<- Back")
        self.product_name = page.locator(".inventory_details_name")

    def click_back_button(self):
        expect(self.back_button).to_be_visible()
        self.back_button.click()

    def verify_product_name(self, expected_text):
        expect(self.product_name).to_contain_text(expected_text)
