from playwright.sync_api import Page

'''
Attributes: Specific link locator
Behaviour: Click on link
'''
class GetLink:
    def __init__(self, page: Page, product_name):
        self.page= page
        self.link = page.get_by_role("link", name=product_name)

    def click_on(self):
        self.link.click()