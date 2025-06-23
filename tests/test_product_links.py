import re
from playwright.async_api import Page
from playwright.sync_api import expect

LOGIN_URL = "https://www.saucedemo.com/v1/index.html"


def test_get_all_product_links(login_logout, page: Page):
    # get all the links from the first page
    links = page.get_by_role("link")
    pattern = re.compile(r"^(Sauce|Test)")
    # filter the links that starts with "Sauce" or "Test"
    product_links = [item for item in links.all_text_contents() if pattern.match(item)]
    print("\nAvailable product links", product_links)
    for product in product_links:
        # click on each link
        print(f"Visiting product: {product}")
        page.get_by_role("link", name=product).click()
        page.wait_for_load_state("networkidle")
        # search to the "back" button and expect to be visible on page
        back_button = page.get_by_role("button", name="<- Back")
        expect(back_button).to_be_visible()
        # go back using the available "back" button
        back_button.click()
        page.wait_for_load_state("networkidle")
