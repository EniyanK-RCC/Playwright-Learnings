import os
import pytest
from dotenv import load_dotenv
from Pages.HomePage.HomePage import HackerrankHomePage
from Pages.LoginPage.LoginPage import HackerrankLoginPage

load_dotenv()

@pytest.mark.usefixtures("setup_and_teardown")
class TestHackerRank:
    """
    A pytest class for executing login functionality on HackerRank's Login Page.
    """

    def test_home(self):
        """
        Tests the navigation from the HackerRank home page to the login page.
        """
        self.url = os.getenv("URL")
        self.homepage = HackerrankHomePage(self.page)
        assert self.homepage.navigate_to_login(self.url)

    def test_login(self):
        """
        Tests the login functionality on HackerRank's Login Page.
        """
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.loginpage = HackerrankLoginPage(self.page)
        assert self.loginpage.login(self.email, self.password)
    