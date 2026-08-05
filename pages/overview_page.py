class OverviewPage:

    def __init__(self, page):
        self.page = page

        self.page_title = ".title"
        self.finish_button = "#finish"
        self.product_names = ".inventory_item_name"

    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()

    def get_product_names(self):
        return self.page.locator(self.product_names).all_inner_texts()

    def click_finish(self):
        self.page.click(self.finish_button)