from utils.json_reader import read_json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

login_data = read_json("data/login_data.json")

def test_valid_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    username = login_data["valid_user"]["username"]
    password = login_data["valid_user"]["password"]

    login_page.open_application()
    login_page.login(username, password)

    actual_title = inventory_page.get_page_title()
    expected_title = "Products"

    assert actual_title == expected_title


def test_invalid_login(page):
    login_page = LoginPage(page)

    username = login_data["invalid_user"]["username"]
    password = login_data["invalid_user"]["password"]

    login_page.open_application()
    login_page.login(username, password)

    actual_error = login_page.get_error_message()
    expected_error = "Epic sadface: Username and password do not match any user in this service"

    assert actual_error == expected_error