class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.page_title = ".title"
        self.cart_icon = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"
        self.backpack_add_button = "#add-to-cart-sauce-labs-backpack"

    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()

    def add_backpack_to_cart(self):
        self.page.click(self.backpack_add_button)

    def get_cart_count(self):
        return self.page.locator(self.cart_badge).inner_text()

    def open_cart(self):
        self.page.click(self.cart_icon)