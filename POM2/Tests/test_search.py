import os
import pytest
from dotenv import load_dotenv
from Pages.GooglePage import GooglePage

load_dotenv()

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    """
    A pytest class for executing search functionality tests on Google's search page.
    """
    def test_search(self):
        """
        Tests the search functionality by navigating to the URL and verifying if recent searches are found.
        """
        self.url = os.getenv("URL")
        self.GooglePage = GooglePage(self.page)
        assert self.GooglePage.search(self.url)