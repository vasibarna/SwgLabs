import logging
import re
from playwright.sync_api import Page, expect
from pages.home_page import GetLink
from pages.product_page import ProductPage


def test_get_all_product_links(authenticated_page, page: Page):
    # get all the links from the first page
    logging.info("Verify the link to the products from the first page")
    links = page.get_by_role("link")
    expect(links.first).to_be_visible()

    # filter the links that starts with "Sauce" or "Test"
    pattern = re.compile(r"^(Sauce|Test)")
    product_links = [item for item in links.all_text_contents() if pattern.match(item)]
    assert len(product_links) != 0, f"No Available links {product_links}"
    logging.info(f"Available links: '{product_links}'")

    # iterate through all the links
    for item in product_links:
        # click on each link and wait for network idle
        logging.info(f"Click on product: {item}")
        link = GetLink(page, item)
        link.click_on()
        page.wait_for_load_state("networkidle")

        # on the new product page, verify the name of the product can be found and click on the back button
        product = ProductPage(page)
        product.verify_product_name(item)
        logging.info(f"'{item}' available on the product page\n")
        product.click_back_button()
        page.wait_for_load_state("networkidle")
