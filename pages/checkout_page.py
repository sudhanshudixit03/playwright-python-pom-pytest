class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name_input = "#first-name"
        self.last_name_input = "#last-name"
        self.postal_code_input = "#postal-code"
        self.continue_button = "#continue"
        self.error_message = "[data-test='error']"

    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)

    def click_continue(self):
        self.page.click(self.continue_button)

    def get_error_message(self):
        return self.page.locator(self.error_message).inner_text()