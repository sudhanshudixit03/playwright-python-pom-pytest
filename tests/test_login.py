from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.open_application()
    login_page.login("standard_user", "secret_sauce")

    actual_url = page.url
    expected_url = "https://www.saucedemo.com/inventory.html"

    assert actual_url == expected_url