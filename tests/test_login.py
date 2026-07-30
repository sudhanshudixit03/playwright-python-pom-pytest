from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open_application()
    login_page.login("standard_user", "secret_sauce")

    actual_title = inventory_page.get_page_title()
    expected_title = "Products"

    assert actual_title == expected_title