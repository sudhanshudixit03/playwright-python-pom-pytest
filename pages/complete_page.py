from pages.base_page import BasePage


class CompletePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = ".title"
        self.confirmation_message = ".complete-header"
        self.back_home_button = "#back-to-products"

    def get_page_title(self):
        return self.get_text(self.page_title)

    def get_confirmation_message(self):
        return self.get_text(self.confirmation_message)

    def click_back_home(self):
        self.click(self.back_home_button)