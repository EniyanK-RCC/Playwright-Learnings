from playwright.sync_api import sync_playwright
from Pages.HomePage.HomePage import Hackerrank_Home_Page
from Pages.LoginPage.LoginPage import Hackerrank_Login_Page

def test_hackerrank_login(url, email, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        homepage = Hackerrank_Home_Page(page)
        loginpage = Hackerrank_Login_Page(page)

        homepage.navigate_to_login(url)
        loginpage.login(email, password)

        browser.close()