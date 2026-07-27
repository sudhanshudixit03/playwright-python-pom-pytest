class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"