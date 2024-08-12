from playwright.sync_api import Page
from Locators.locators import Locator
from Configs.LogConfig import logger

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
        logger.info(f"Navigating to {url}")
        self.page.goto(url)

        logger.info("Clicking on the login")
        self.locator.get_locator("login_locator").click()

        logger.info("Clicking on the developer login")
        self.locator.get_locator("dev_login_locator").click()

        if self.locator.get_locator("email_locator"):
            logger.info("Test 1 passed")
            return True
        else:
            logger.error("Test 1 failed")
            return False