from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = ".title"
        self.cart_items = ".cart_item"
        self.product_name = ".inventory_item_name"
        self.remove_backpack_button = "#remove-sauce-labs-backpack"
        self.checkout_button = "#checkout"

    def get_page_title(self):
        return self.get_text(self.page_title)

    def get_product_name(self):
        return self.get_text(self.product_name)

    def get_cart_items_count(self):
        return self.get_count(self.cart_items)

    def remove_backpack(self):
        self.click(self.remove_backpack_button)

    def click_checkout(self):
        self.click(self.checkout_button)