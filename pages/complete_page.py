class CompletePage:

    def __init__(self, page):
        self.page = page

        self.page_title = ".title"
        self.confirmation_message = ".complete-header"
        self.back_home_button = "#back-to-products"

    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()

    def get_confirmation_message(self):
        return self.page.locator(self.confirmation_message).inner_text()

    def click_back_home(self):
        self.page.click(self.back_home_button)