import re
from playwright.async_api import Page
from playwright.sync_api import expect


def test_add_products_in_cart(login_logout, page: Page):
    # verify the shopping cart is empty
    shopping_cart = page.locator("#shopping_cart_container").get_by_role("link")
    expect(shopping_cart).to_be_visible()
    assert shopping_cart.get_attribute("name") in [None, 0, False, "0", "False", ""]

    # get all the links from the first page
    links = page.get_by_role("link")
    pattern = re.compile(r"^(Sauce|Test)")
    # filter the links that starts with "Sauce" or "Test"
    product_links = [item for item in links.all_text_contents() if pattern.match(item)]
    # iterate through all the products and add them to the shopping cart
    for i, product in enumerate(product_links):
        # click on each link and add the product to cart
        print(f"Visiting product: {product}")
        page.get_by_role("link", name=product).click()
        page.wait_for_load_state("networkidle")
        # add the product to the cart
        print("Add product to the cart: ", {product})
        page.get_by_role("button", name="ADD TO CART").click()
        # verify the shopping cart
        shopping_cart = page.locator("span.fa-layers-counter.shopping_cart_badge")
        assert int(shopping_cart.text_content()) == i+1
        if i == 1:
            print(f"Shopping Cart contains {i+1} product")
        else:
            print(f"Shopping Cart contains {i + 1} products")
        # go back using the available "page back" button
        page.go_back()
        page.wait_for_load_state("networkidle")


def test_remove_products_from_cart(login_logout, page: Page):
    # get all the links from the first page
    links = page.get_by_role("link")
    pattern = re.compile(r"^(Sauce|Test)")
    # filter the links that starts with "Sauce" or "Test"
    product_links = [item for item in links.all_text_contents() if pattern.match(item)]
    # iterate through all the products and add them to the shopping cart
    for i, product in enumerate(product_links):
        # click on each link and add the product to cart
        page.get_by_role("link", name=product).click()
        page.wait_for_load_state("networkidle")
        page.get_by_role("button", name="ADD TO CART").click()
        page.go_back()
        page.wait_for_load_state("networkidle")

    # Shopping cart products number
    page.goto("https://www.saucedemo.com/v1/cart.html")
    remove_buttons = page.get_by_role("button", name="REMOVE")
    for i in reversed(range(remove_buttons.count())):
        print(f"Removing item {i + 1}")
        remove_buttons.nth(i).click()
    # verify the shopping cart is empty
    shopping_cart = page.locator("#shopping_cart_container").get_by_role("link")
    expect(shopping_cart).to_be_visible()
    assert shopping_cart.get_attribute("name") in [None, 0, False, "0", "False", ""]
