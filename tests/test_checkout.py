from utils.json_reader import read_json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage

checkout_data = read_json("data/checkout_data.json")

login_data = read_json("data/login_data.json")

def test_complete_checkout_process(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = OverviewPage(page)
    complete_page = CompletePage(page)

    login_page.open_application()
    login_page.login(
        login_data["valid_user"]["username"],
        login_data["valid_user"]["password"]
    )

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    actual_cart_count = inventory_page.get_cart_count()
    expected_cart_count = 1

    assert actual_cart_count == expected_cart_count

    inventory_page.go_to_cart()

    actual_cart_title = cart_page.get_page_title()
    expected_cart_title = "Your Cart"

    assert actual_cart_title == expected_cart_title

    cart_page.click_checkout()

    checkout_page.enter_checkout_information(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["postal_code"]
    )
    checkout_page.click_continue()

    actual_overview_title = overview_page.get_page_title()
    expected_overview_title = "Checkout: Overview"

    assert actual_overview_title == expected_overview_title

    actual_product_names = overview_page.get_product_names()
    expected_product_names = ["Sauce Labs Backpack"]

    assert actual_product_names == expected_product_names

    overview_page.click_finish()

    actual_complete_title = complete_page.get_page_title()
    expected_complete_title = "Checkout: Complete!"

    assert actual_complete_title == expected_complete_title

    actual_confirmation_message = complete_page.get_confirmation_message()
    expected_confirmation_message = "Thank you for your order!"

    assert actual_confirmation_message == expected_confirmation_message