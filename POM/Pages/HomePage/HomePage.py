from playwright.sync_api import Page
from Locators.locators import Locator

class HackerrankHomePage:
    """
    A Page object model class for interacting with HackerRank's Home Page.
    """
    def __init__(self, page: Page):
        """
        Initializes the HackerrankHomePage with a Page and Locator instance.

        Args:
            page (Page): The Playwright Page object representing the browser page.
        """
        self.page = page
        self.locator = Locator(page)
        
    def navigate_to_login(self, url):
        """
        Navigates to the login page and performs actions to initiate the login process.
        """
        self.page.goto(url)
        self.locator.get_locator("login_locator").click()
        self.locator.get_locator("dev_login_locator").click()

    