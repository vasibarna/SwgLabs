import logging
import re
from playwright.sync_api import Page
from playwright.sync_api import expect


def test_all_links(authenticated_page, page: Page):
    # get all the links from the first page
    logging.info("Verify all the links from the first page")
    links = page.get_by_role("link")
    pattern = re.compile(r"^[A-KM-Za-km-z].*")
    # filter the links that starts with letter, except letter "L"=Logout
    all_links = [item for item in links.all_text_contents() if pattern.match(item)]
    if len(all_links) != 0:
        logging.info(f"\nAvailable links: '{all_links}'")
    else:
        logging.warning(f"\n No Available links: '{all_links}'")
    for product in all_links:
        if product in ["All Items"]:
            logging.info(f"Visiting link: {product}")
            page.get_by_role("button", name="Open Menu").click()
            page.get_by_role("link", name=product).click()
            page.wait_for_load_state("networkidle")
            expect(page.get_by_role("combobox")).to_be_visible()
        elif product in ["About"]:
            logging.info(f"Visiting link: {product}")
            page.get_by_role("button", name="Open Menu").click()
            page.get_by_role("link", name=product).click()
            page.wait_for_load_state("networkidle")
            expect(page.get_by_role("button", name="Sign in")).to_be_visible()
            expect(page.get_by_role("link", name="Saucelabs")).to_be_visible()
#            expect(page.get_by_role("button", name="Accept All Cookies")).to_be_visible()
            expect(page.get_by_role("button", name="search")).to_be_visible()
            page.go_back()
            page.wait_for_load_state("networkidle")
        else:
            # click on each link from products
            logging.info(f"Visiting link: {product}")
            page.get_by_role("link", name=product).click()
            page.wait_for_load_state("networkidle")
            # search to the "back" button and expect to be visible on page
            back_button = page.get_by_role("button", name="<- Back")
            expect(back_button).to_be_visible()
            # go back using the available "back" button
            back_button.click()
            page.wait_for_load_state("networkidle")
