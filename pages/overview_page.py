from pages.base_page import BasePage


class OverviewPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = ".title"
        self.finish_button = "#finish"
        self.product_names = ".inventory_item_name"

    def get_page_title(self):
        return self.get_text(self.page_title)

    def get_product_names(self):
        return self.page.locator(self.product_names).all_inner_texts()

    def click_finish(self):
        self.click(self.finish_button)