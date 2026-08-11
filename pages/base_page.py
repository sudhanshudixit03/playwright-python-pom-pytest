from utils.logger import get_logger


class BasePage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url):
        self.logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.logger.info(f"Entering value in element: {locator}")
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        self.logger.info(f"Getting text from element: {locator}")
        return self.page.locator(locator).inner_text()

    def get_count(self, locator):
        self.logger.info(f"Getting count for locator: {locator}")
        return self.page.locator(locator).count()

    def is_visible(self, locator):
        self.logger.info(f"Checking visibility of element: {locator}")
        return self.page.locator(locator).is_visible()