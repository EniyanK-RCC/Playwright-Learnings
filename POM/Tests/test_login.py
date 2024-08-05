import os
import pytest
from dotenv import load_dotenv
from Pages.HomePage.HomePage import Hackerrank_Home_Page
from Pages.LoginPage.LoginPage import Hackerrank_Login_Page

load_dotenv()

@pytest.mark.usefixtures("setup_and_teardown")
class TestHackerRank:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.url = os.getenv("URL")
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.homepage = Hackerrank_Home_Page(self.page)
        self.loginpage = Hackerrank_Login_Page(self.page)

    def test_home(self):
        self.homepage.navigate_to_login(self.url)

    def test_login(self):
        self.loginpage.login(self.email, self.password)
    