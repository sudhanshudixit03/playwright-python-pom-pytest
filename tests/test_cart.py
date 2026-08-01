from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_single_product_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open_application()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    actual_cart_count = inventory_page.get_cart_count()
    expected_cart_count = "1"

    assert actual_cart_count == expected_cart_count

    inventory_page.open_cart()

    actual_cart_title = cart_page.get_page_title()
    expected_cart_title = "Your Cart"

    assert actual_cart_title == expected_cart_title

    actual_product_name = cart_page.get_product_name()
    expected_product_name = "Sauce Labs Backpack"

    assert actual_product_name == expected_product_name




def test_remove_product_from_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open_application()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page.remove_backpack()

    actual_cart_items = cart_page.get_cart_items_count()
    expected_cart_items = 0

    assert actual_cart_items == expected_cart_items