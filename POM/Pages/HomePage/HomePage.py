from playwright.sync_api import Page
from Locators.locators import Locator

class Hackerrank_Home_Page:
    def __init__(self, page: Page):
        self.page = page
        self.locator = Locator(page)
        
    def navigate_to_login(self, url):
        self.page.goto(url)
        self.locator.login_locator().click()
        self.locator.dev_login_locator().click()

    