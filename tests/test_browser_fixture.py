def test_browser_fixture(page):
    page.goto("https://www.saucedemo.com/")

    actual_title = page.title()

    assert actual_title == "Swag Labs"