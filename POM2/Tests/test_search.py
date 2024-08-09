import os
import pytest
from dotenv import load_dotenv
from Pages.GooglePage import googlePage

load_dotenv()

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.url = os.getenv("URL")
        self.googlePage = googlePage(self.page)
    def test_search(self):
        assert self.googlePage.search(self.url)