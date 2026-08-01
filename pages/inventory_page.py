class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.page_title = ".title"
        self.cart_icon = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"

    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()

    def add_product_to_cart(self, product_name):
        product = self.page.locator(
            ".inventory_item"
        ).filter(has_text=product_name)

        product.get_by_role("button", name="Add to cart").click()

    def get_cart_count(self):
        return self.page.locator(self.cart_badge).inner_text()

    def open_cart(self):
        self.page.click(self.cart_icon)