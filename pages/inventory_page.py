from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = ".title"
        self.cart_icon = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"
        self.inventory_items = ".inventory_item"

    def get_page_title(self):
        return self.get_text(self.page_title)

    def add_product_to_cart(self, product_name):
        self.logger.info(f"Adding product to cart: {product_name}")

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
        return int(self.get_text(self.cart_badge))

    def go_to_cart(self):
        self.click(self.cart_icon)