from playwright.sync_api import sync_playwright
from Hackerrank_page import Hackerrank_Login_Page

def test_hackerrank_login(url, email, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        hackerrank_page = Hackerrank_Login_Page(page)

        hackerrank_page.login_page(url)
        hackerrank_page.login(email, password)

        browser.close()