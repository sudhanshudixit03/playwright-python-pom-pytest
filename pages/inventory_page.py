class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.page_title = ".title"
        self.cart_icon = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"
        self.inventory_items = ".inventory_item"

    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()

    def add_product_to_cart(self, product_name):
        product = self.page.locator(
            self.inventory_items
        ).filter(has_text=product_name)

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

    def add_products_to_cart(self, product_names):
        for product_name in product_names:
            self.add_product_to_cart(product_name)

    def get_cart_count(self):
        return int(
            self.page.locator(
                self.cart_badge
            ).inner_text()
        )

    def go_to_cart(self):
        self.page.locator(
            self.cart_icon
        ).click()