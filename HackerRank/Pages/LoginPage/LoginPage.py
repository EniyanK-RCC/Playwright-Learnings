from playwright.sync_api import Page
from Locators.locators import Locator
from Configs.LogConfig import logger

class HackerrankLoginPage:
    """
    A Page object model class for interacting with HackerRank's Login Page.
    """
    def __init__(self, page: Page):
        """
        Initializes the HackerrankLoginPage with a Page and Locator instance.

        Args:
            page (Page): The Playwright Page object representing the browser page.
        """
        self.page = page
        self.locator = Locator(page)

    def login(self, username_or_email, password):
        """
        Performs login operation by filling the username and password in the input area.
        """
        logger.info("Filling up the email")
        self.locator.get_locator("email_locator").fill(username_or_email)

        logger.info("Filling up the password")
        self.locator.get_locator("password_locator").fill(password)

        logger.info("Clicking on the login button")
        self.locator.get_locator("final_login").click()

        if self.locator.get_locator("prepare_locator"):
            logger.info("Test 2 passed")
            return True
        else:
            logger.error("Test 2 failed")
            return False