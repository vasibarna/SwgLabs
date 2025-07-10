import logging
import re
from playwright.sync_api import Page
from playwright.sync_api import expect
from pages.home_page import GetLink
from pages.open_menu_page import OpenMenu
from pages.sauce_labs_page import SauceLab


def test_open_menu_links(authenticated_page, page: Page):
    # get all the links from the first page
    logging.info("Verify all the links from the first page")
    links = page.get_by_role("link")
    expect(links.first).to_be_visible()

    # filter the links that start with letter A. "All Items" and "About" are looked for.
    pattern = re.compile(r"^A.*")
    all_links = [item for item in links.all_text_contents() if pattern.match(item)]
    assert len(all_links) != 0, f"No Available links {all_links}"
    logging.info(f"Open Menu Links: '{all_links}'")

    # Iterate through the links, click on each and expect some elements to be visible
    for product in all_links:
        if product in ["All Items"]:
            logging.info(f"Click on link: {product}")
            open_menu = OpenMenu(page)
            open_menu.click_open_menu_button()
            link = GetLink(page, product)
            link.click_on()
            page.wait_for_load_state("networkidle")
            expect(page.get_by_role("combobox")).to_be_visible()
        else:
            logging.info(f"Click on link: {product}")
            open_menu = OpenMenu(page)
            open_menu.click_open_menu_button()
            link = GetLink(page, product)
            link.click_on()
            page.wait_for_load_state("networkidle")
            sauce_lab = SauceLab(page)
            sauce_lab.verify_sign_in_button()
            sauce_lab.verify_sign_in_button()
            try:
                page.go_back()
                page.wait_for_url("**/inventory.html")
            except Exception as e:
                logging.warning(f"Fallback navigation due to error: {e}")
                page.goto("https://www.saucedemo.com/v1/inventory.html")
