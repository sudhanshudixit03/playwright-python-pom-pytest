class CartPage:

    def __init__(self, page):
        self.page = page

        self.page_title = ".title"
        self.cart_items = ".cart_item"
        self.product_name = ".inventory_item_name"
        self.remove_backpack_button = "#remove-sauce-labs-backpack"
        self.checkout_button = "#checkout"

    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()

    def get_product_name(self):
        return self.page.locator(self.product_name).inner_text()

    def get_cart_items_count(self):
        return self.page.locator(self.cart_items).count()

    def remove_backpack(self):
        self.page.click(self.remove_backpack_button)

    def click_checkout(self):
        self.page.click(self.checkout_button)