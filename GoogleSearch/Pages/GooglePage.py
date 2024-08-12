from playwright.sync_api import Page
from Locators.locators import Locator
from Configs.LogConfig import logger

class GooglePage:
    """
    A page object model class for interacting with Google's search page.
    """
    def __init__(self, page: Page):
        """
        Initializes the GooglePage with a Page and Locator instance.

        Args:
            page (Page): The Playwright Page object representing the browser page.
        """
        self.page = page
        self.locator = Locator(page)

    def search(self, url):
        """
        Navigates to the specified URL, interacts with the search bar, fetches recent searches, 
        logs the recent searches, and writes them to a file.

        Args:
            url (str): The URL to navigate to.
        """

        logger.info(f"Navigating to {url}")
        self.page.goto(url)

        logger.info("Clicking on the search bar")
        self.locator.get_locator("search_bar").click()

        logger.info("Fetching recent searches")
        recent_searches = self.locator.get_locator("presentation_locator").all_text_contents()[:10]

        for index, search in enumerate(recent_searches, start=1):
            logger.info(f"{index}: {search}")

        # writing the recent searches in a file
        with open("recent_searches.txt", "w") as file:
            for index, search in enumerate(recent_searches, start=1):
                file.write(f"{index}: {search}\n")

        if len(recent_searches) > 0:
            logger.info("Recent searches found")
            return True
        else:
            logger.warning("No recent searches found")
            return False
