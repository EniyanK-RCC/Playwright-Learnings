from playwright.sync_api import Page

class Hackerrank_Home_Page:
    def __init__(self, page: Page):
        self.page = page
        
    def navigate_to_login(self, url):
        self.page.goto(url)
        self.page.get_by_role("link", name="Log in").click()
        self.page.get_by_role("link", name="Login").nth(1).click()

    