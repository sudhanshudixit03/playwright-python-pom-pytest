from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.first_name_input = "#first-name"
        self.last_name_input = "#last-name"
        self.postal_code_input = "#postal-code"
        self.continue_button = "#continue"
        self.error_message = "[data-test='error']"

    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)
        self.fill(self.postal_code_input, postal_code)

    def click_continue(self):
        self.click(self.continue_button)

    def get_error_message(self):
        return self.get_text(self.error_message)