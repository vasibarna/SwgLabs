from playwright.sync_api import Page, expect

''' 
Attributes: Back button and product name locators
Behaviour: Click on back button or verify if 'expected name' is contained in 'product name'
'''
class ProductPage:
    def __init__(self, page: Page):
        self.page= page
        self.back_button = page.get_by_role("button", name="<- Back")
        self.product_name = page.locator(".inventory_details_name")

    def click_back_button(self):
        self.back_button.click()

    def verify_product_name(self, expected_text):
        expect(self.product_name).to_contain_text(expected_text)
