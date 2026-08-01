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


def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.open_application()
    login_page.login("invalid_user", "invalid_password")

    actual_error = login_page.get_error_message()
    expected_error = (
        "Epic sadface: Username and password do not match any user in this service"
    )

    assert actual_error == expected_error